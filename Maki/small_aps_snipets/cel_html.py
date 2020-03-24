from os import path
from bs4 import BeautifulSoup
import requests
import memcache
from datetime import datetime
from datetime import date
from http.server import HTTPServer, BaseHTTPRequestHandler


today = date.today()

URL = "https://www.facebook.com/"

server_IP = "0.0.0.0"
my_server_IP = "0.0.0.0"

key_c = "content_"
key_date = "last_datetime_"

cache = memcache.Client(server_IP)


def main():
    run(HTTPServer, BaseHTTPRequestHandler)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str_to_bin((get_content())))


def run(server_class, handler_class):
    httpd = HTTPServer((my_server_IP, 2020), SimpleHTTPRequestHandler)
    httpd.serve_forever()


def get_content():
    last_date = cache.get(key_date)

    if last_date is None or (datetime.today() - last_date).seconds > (5 * 60):
        content = requests.get(URL)
        cache.set(key_c, content)

    content = cache.get(key_c)

    if content is None:
        content = requests.get(URL)
    set_date_to_mc()
    print(type(BeautifulSoup(content.text, "html.parser")))
    return content.text


def scrape_stats(content):
    soup = BeautifulSoup(content.text, "html.parser")
    table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
    table_stats[0] = str(today)
    stats_csv = str.join(",", table_stats)
    return stats_csv


def str_to_bin(string):
    return bytes(string, 'utf-8')


def set_date_to_mc():
    cache.set(key_date, datetime.today())


if __name__ == "__main__":
    main()
