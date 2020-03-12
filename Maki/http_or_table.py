from os import path
from bs4 import BeautifulSoup
import requests
import memcache
from datetime import datetime
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler


names_csv = "Date,Total Cases,New Cases,Total Deaths,New Deaths," \
            "Total Recovered,Active cases,Serious/Critical" \
            ",Total Cases per 1M"

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K" \
      "4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"

server_IP = "127.0.0.1"
my_server_IP = "0.0.0.0"
port = 2021

file_name = "stats_covid19.csv"

key_c = "content"
key_date = "last_datetime"

cache = memcache.Client(server_IP)

last_hour = cache.get(key_date)


def main():
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
        self.end_headers()
        update_table()
        self.wfile.write(str_to_bin(scrape_stats(get_content())))


def run(server_class, handler_class):
    httpd = HTTPServer((my_server_IP, port), SimpleHTTPRequestHandler)
    httpd.serve_forever()


def align_left(string):
    return str.join("", [str.ljust(s, 18) + "|" for s in string.split(',')])


def str_to_bin(string):
    return bytes(align_left(names_csv) + '\n' + align_left(string) + '\n', 'ASCII')


def get_lines_from_file():
    f = open(file_name, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_content():
    last_date = cache.get(key_date)
    print("Seconds passed since last update: " + str((datetime.today() - last_date).seconds) + "s")
    if last_date is None or is_cache_outdated(last_date):
        print("Content updated. 5 minutes have passed since last cache")
        content = requests.get(URL)
        set_date_to_cache()
        set_content_to_cache(content)

    content = cache.get(key_c)

    if content is None:
        content = requests.get(URL)

    return content


def scrape_stats(content):
    soup = BeautifulSoup(content.text, "html.parser")
    table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
    table_stats[0] = str(format_date(last_hour) + "h")
    stats_csv = str.join(",", table_stats)
    return stats_csv


def new_file(content, is_request):
    write_to_file(content, names_csv)

    print("Created new file: {}".format(format_date(cache.get(key_date))))
    print(content)
    if not is_request:
        exit(1)


def edit_content(stats, lines):
    if not is_up_to_date(last_hour, lines[-1]):
        print("Added entry for {}".format(format_date(last_hour)))
        lines.append(stats + '\n')

    elif lines[-1].strip() != stats.strip():
        print("Updated for {}h".format(format_date(last_hour)))
        lines[-1] = stats + '\n'

    else:
        print("File is up to date:")
        print('[', stats, ']', sep='')

    write_to_file(lines)


def set_date_to_cache():
    cache.set(key_date, datetime.today())


def set_content_to_cache(content):
    cache.set(key_c, content)


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


def is_cache_outdated(last_date):
    if (datetime.today() - last_date).seconds > (5 * 60):
        return True
    lines = get_lines_from_file()
    return format_date(last_date) not in lines[-1]


if __name__ == "__main__":
    main()
