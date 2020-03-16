from os import path
from bs4 import BeautifulSoup
import requests
import memcache
from datetime import datetime
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from dateutil.parser import parse as parsedate
import sqlite

_db = None
DB_FILE = "covid19.db"
TABLE_NAME = "covid19"

def db_connection(db_file=DB_FILE):
    if not _db:
        _db = sqlite.connect(DB_FILE)
    return _db


def insert_row(values):
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("INSER INTO {} VALUES {}".format(TABLE_NAME, values))
    db.commit()


def read_row():
    """ This should return a list of the values for a row"""
    db = db_connection()
    cursor = db.cursor()
    result = cursor.execute("SELECT * FROM {}".format(TABLE_NAME)
    return result


names_csv = "Date,Total Cases,New Cases,Total Deaths,New Deaths," \
            "Total Recovered,Active cases,Serious/Critical" \
            ",Total Cases per 1M"

c.execute('''CREATE TABLE covid19
             (date text, 
              country text,
              total_cases real, 
              new_cases real, 
              togal_deaths real, 
              new_deaths real)''')

c.execute('''INSERT INTO covid19
             VALUES('2020-03-16T11:41:42.567789',
             12341234,
             1234,
             12341234,
             1234)''')


URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K" \
      "4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"

server_IP = "127.0.0.1"
my_server_IP = "0.0.0.0"
port = 2021

file_name = "stats_covid19.csv"

key_c = "content"
key_date = "last_datetime_key"
key_header = 'key_header'

cache = memcache.Client(server_IP)

last_date = cache.get(key_date)


def main():
    global last_date
    if last_date is None:
        last_date = set_date_to_cache()

    # TESTcache.get(key_header)
    run(HTTPServer, BaseHTTPRequestHandler)

    if len(sys.argv) > 1 and sys.argv[1] == '--https':
        run(HTTPServer, BaseHTTPRequestHandler)
    # if --https is sent as argument the program stops here

    update_table()


def update_table(is_request=False):
    content = get_content()

    stats_csv = scrape_stats(content)

    if not path.exists(file_name):
        new_file(stats_csv, is_request)

    # If the file was just created the program finishes here=======================

    lines = get_lines_from_file()

    if len(lines) == 0:
        new_file(stats_csv, is_request)

    # If the file was just created the program finishes here=======================

    edit_content(stats_csv, lines)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header('last-modified', last_date)
        self.send_header('content-type', "application/json")
        self.end_headers()

        update_table()
        try:
            self.wfile.write(str_to_bin(scrape_stats(get_content())))
        except BrokenPipeError:
            print(BrokenPipeError.args)


def run(server_class, handler_class):
    httpd = HTTPServer((my_server_IP, port), SimpleHTTPRequestHandler)
    httpd.serve_forever()


def align_left(string):
    return str.join("", [str.ljust(s, 18) + "|" for s in string.split(',')])


def str_to_bin(string):
    return format_to_json(names_csv, string)


def get_lines_from_file():
    f = open(file_name, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_header(header):
    if header is None or header["last-modified"] is None or header["last-modified"] != last_date:
        header["last-modified"] = last_date
        cache.set(key_header, header)
    return header['last-modified']


def get_content():
    global last_date
    last_date = cache.get(key_date)
    if last_date is None or not path.exists(file_name) or is_cache_outdated():
        print("Content updated. 5 minutes have passed since last cache")
        content = requests.get(URL)
        last_date = set_date_to_cache()
        set_content_to_cache(content)

    print("Seconds passed since last update: " + str((datetime.today() - last_date).seconds) + "s")
    content = cache.get(key_c)

    if content is None:
        content = requests.get(URL)

    return content


def scrape_stats(content):
    soup = BeautifulSoup(content.text, "html.parser")
    table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
    table_stats[0] = str(format_date(last_date) + "h")
    stats_csv = str.join(",", table_stats)
    return stats_csv


def new_file(content, is_request):
    write_to_file(content, names_csv)

    print("Created new file: {}".format(format_date(cache.get(key_date))))
    print(content)
    if not is_request:
        exit(1)


def edit_content(stats, lines):
    if not is_up_to_date(last_date, lines[-1]):
        print("Added entry for {}".format(format_date(last_date)))
        lines.append(stats + '\n')

    elif lines[-1].strip() != stats.strip():
        print("Updated for {}h".format(format_date(last_date)))
        lines[-1] = stats + '\n'

    else:
        print("File is up to date:")
        print('[', stats, ']', sep='')

    write_to_file(lines)


def set_date_to_cache():
    cache.set(key_date, datetime.today())
    return cache.get(key_date)


def set_content_to_cache(content):
    cache.set(key_c, content)


def format_to_json(names, data):
    list_names = names.split(',')
    list_data = data.split(',')
    dict_data = dict(zip(list_names, list_data))
    return json.dumps(dict_data).encode()


def write_to_file(content, names=None):
    f = open(file_name, "w")

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


def is_cache_outdated():
    if (datetime.today() - last_date).seconds > (5 * 60):
        return True
    lines = get_lines_from_file()
    return format_date(last_date) not in lines[-1]


if __name__ == "__main__":
    main()
