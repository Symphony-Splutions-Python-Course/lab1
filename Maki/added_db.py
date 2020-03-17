from os import path
from bs4 import BeautifulSoup
import requests
import memcache
from datetime import datetime
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sqlite3 as sql

ATTRIBUTE_NAMES = 'Date,Total_Cases,New_Cases,Total_Deaths,New_Deaths,Total_Recovered,Active_cases,' \
                  'Serious_or_Critical,' \
                  'Total_Cases_per_1M '

ATTRIBUTE_NAMES_DB = 'Date,Total_Cases text,New_Cases integer,Total_Deaths integer,New_Deaths integer,Total_Recovered integer,Active_cases integer,' \
                     'Serious_or_Critical integer,' \
                     'Total_Cases_per_1M real'

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K" \
      "4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"

LOCAL_SERVER_IP = "127.0.0.1"
PUBLIC_SERVER_IP = "0.0.0.0"
PORT_NUMBER = 2021
CSV_FILE_NAME = "stats_covid19.csv"
DATABASE_NAME = "covid19.db"
COVID_TABLE = "covid_19"

STATS_DB_KEY = "stats_db"
STATS_KEY = "stats"
DATE_KEY = "last_datetime_key"
HEADER_KEY = 'key_header'
DATABASE_KEY = "db_key1"

CACHE = memcache.Client(LOCAL_SERVER_IP)

my_db = None

LAST_UPDATED_DATE = CACHE.get(DATE_KEY)


def main():
    global LAST_UPDATED_DATE

    if LAST_UPDATED_DATE is None:
        LAST_UPDATED_DATE = set_date_to_cache()

    if len(sys.argv) > 1:
        if sys.argv[1] == '--https':
            run()

    # if --https is sent as argument the program stops here
    update()


def update_database():
    global my_db
    if my_db is None:
        my_db = Database()
        my_db.create_table(COVID_TABLE, ATTRIBUTE_NAMES_DB)
        my_db.update(get_stats(db=True), COVID_TABLE)
    if not my_db.is_up_to_date():
        stats = get_stats()
        my_db.update(stats, COVID_TABLE)


class Database:
    # how to make Database inherit and also put new fields?
    def __init__(self):
        self.tables = dict()
        self.last_row = None
        self.connection = sql.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()

    def execute(self, command, values=None):
        print(command)
        if values is None:
            self.cursor.execute(command)
            return
        self.cursor.execute(command, values)

    def commit(self):
        self.connection.commit()

    def add_row_input(self):
        self.execute("INSERT INTO " + input("Enter table name:").strip() + " VALUES" +
                     "(" + self.input_row() + ")")
        print("INSERT INTO " + input("Enter table name:").strip() + " VALUES" +
              "(" + self.input_row() + ")")

    def add_row(self, values, table_name):
        table_name = table_name.strip()
        print(values)
        self.execute("INSERT INTO " + table_name + " VALUES(" + values + ")")
        self.commit()

    def create_table_input(self):
        table_name = input("Enter table name: ")
        attributes = self.input_table()
        self.execute("CREATE TABLE " + input("Enter table name: ") + "(" + attributes + ")")
        self.tables[table_name] = attributes
        self.commit()

    def create_table(self, table_name, att):
        try:
            self.execute("CREATE TABLE " + table_name.strip() + "(" + att.strip() + ")")
            print("CREATE TABLE " + table_name + "(" + att + ")")
        except sql.OperationalError:
            print("Table exists")

    def show_tables(self):
        print(self.tables)

    def read_all(self):
        return self.execute("SELECT * FROM " + DATABASE_NAME)

    def update(self, stats, table):
        self.add_row(stats, table_name=table)

    @staticmethod
    def is_up_to_date():
        global LAST_UPDATED_DATE
        if LAST_UPDATED_DATE is None:
            LAST_UPDATED_DATE = datetime.now()
            return False
        if format_date(datetime.now()) != format_date(LAST_UPDATED_DATE):
            return False
        return True

    @staticmethod
    def print(self, result):
        for row in result:
            print(row)

    def select(self, attributes, table_name, conditions):
        if attributes.strip() == 0:
            print("Nothing entered for table")
            return None

        if table_name not in str(self.tables.keys()):
            print("No such table")
            return None

        for att in attributes.split(","):
            if att.strip() not in self.tables[table_name]:
                return None

        if len(conditions.strip()) == 0:
            return self.execute("SELECT " + attributes + " FROM " + table_name)
        return self.execute("SELECT " + attributes + " FROM " + table_name + " WHERE " + conditions)

    def select_input(self):
        attributes = input("Select attributes: ")
        table_name = input("From table: ")
        conditions = input("Where(Leave empty to skip): ")
        self.select(attributes, table_name, conditions)

        # TODO: set number of attributes according to the number of columns in the table

    def input_row(self, table_name):
        new_row = list()
        for att in self.tables[table_name]:
            new_row.append(input("Enter value for" + att + ": ").strip())
        return str.join(",", new_row)

    @staticmethod
    def input_table():
        n = input("Enter number of attributes: ")
        l = []
        for i in range(n):
            att = input("Enter attribute name: ")
            att_type = input("Enter attribute type: ")
            l.append(att + " " + att_type)
        return str.join(",", l)


def update_table(is_request=False):
    stats = get_stats()

    if not path.exists(CSV_FILE_NAME):
        new_file(stats, is_request)

    # If the file was just created the program finishes here=======================

    lines = get_lines_from_file()

    if len(lines) == 0:
        new_file(stats, is_request)

    # If the file was just created the program finishes here=======================

    edit_content(stats, lines)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header('last-modified', LAST_UPDATED_DATE)
        self.send_header('content-type', "application/json")
        self.end_headers()

        update()
        try:
            self.wfile.write(str_to_bin(scrape_stats(get_stats())))
        except BrokenPipeError:
            print(BrokenPipeError.args)


def run():
    httpd = HTTPServer((PUBLIC_SERVER_IP, PORT_NUMBER), SimpleHTTPRequestHandler)
    httpd.serve_forever()


def align_left(string):
    return str.join("", [str.ljust(s, 18) + "|" for s in string.split(',')])


def str_to_bin(string):
    return format_to_json(ATTRIBUTE_NAMES, string)


def get_lines_from_file():
    f = open(CSV_FILE_NAME, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_header(header):
    if header is None or header["last-modified"] is None or header["last-modified"] != LAST_UPDATED_DATE:
        header["last-modified"] = LAST_UPDATED_DATE
        CACHE.set(HEADER_KEY, header)
    return header['last-modified']


def get_stats(db=False):
    global LAST_UPDATED_DATE
    stats_for_db = None
    LAST_UPDATED_DATE = CACHE.get(DATE_KEY)
    if LAST_UPDATED_DATE is None or not path.exists(CSV_FILE_NAME) or is_stats_cache_outdated():
        content = requests.get(URL)
        LAST_UPDATED_DATE = set_date_to_cache()
        stats_for_db = scrape_stats(content, db=True)
        set_stats_to_cache(scrape_stats(content), stats_for_db)

    print("Seconds passed since last update: " + str((datetime.today() - LAST_UPDATED_DATE).seconds) + "s")
    content = CACHE.get(STATS_KEY)

    if content is None:
        content = requests.get(URL)

    if db is True:
        return str.join(",", CACHE.get(STATS_DB_KEY)).replace(" ", "_")

    return str.join(",",content)


def scrape_stats(content, db=False):
    soup = BeautifulSoup(content.text, "html.parser")
    table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
    table_stats[0] = str(format_date(LAST_UPDATED_DATE) + "h")
    stats_csv = str.join(",", table_stats)
    if db is True:
        table_stats[0] = "\"" + table_stats[0] + "\""
        return table_stats
    return table_stats


def new_file(content, is_request):
    write_to_file(content, ATTRIBUTE_NAMES)

    print("Created new file: {}".format(format_date(CACHE.get(DATE_KEY))))
    print(content)
    if not is_request:
        exit(1)


def edit_content(stats, lines):
    if not is_up_to_date(LAST_UPDATED_DATE, lines[-1]):
        print("Added entry for {}".format(format_date(LAST_UPDATED_DATE)))
        lines.append(stats + '\n')

    elif lines[-1].strip() != stats.strip():
        print("Updated for {}h".format(format_date(LAST_UPDATED_DATE)))
        lines[-1] = stats + '\n'

    else:
        print("File is up to date:")
        print('[', stats, ']', sep='')

    write_to_file(lines)


def set_date_to_cache():
    CACHE.set(DATE_KEY, datetime.today())
    return CACHE.get(DATE_KEY)


def set_stats_to_cache(content, stats_db):
    CACHE.set(STATS_KEY, content)
    CACHE.set(STATS_DB_KEY, stats_db)

def format_to_json(names, data):
    list_names = names.split(',')
    list_data = data.split(',')
    dict_data = dict(zip(list_names, list_data))
    return json.dumps(dict_data).encode()


def write_to_file(content, names=None):
    f = open(CSV_FILE_NAME, "w")

    if names is not None:
        f.write(names + "\n")
        f.write(content + "\n")

    else:
        f.write(str.join("", content))

    f.close()


def format_date(date):
    return date.strftime("%b %d %Y %H")


def is_up_to_date(date_h, line):
    return format_date(date_h) in line


def is_stats_cache_outdated():
    if (datetime.today() - LAST_UPDATED_DATE).seconds > (5 * 60):
        print("5 minutes have passed since last cache. Stats updated.")
        return True
    lines = get_lines_from_file()
    return format_date(LAST_UPDATED_DATE) not in lines[-1]


def update():
    global LAST_UPDATED_DATE
    update_database()
    update_table()
    LAST_UPDATED_DATE = datetime.now()


if __name__ == "__main__":
    main()
