import sys
from http.server import HTTPServer
import os
from my_helpers.cache_handler import set_date_to_cache, get_last_date
from my_helpers.constants import DATABASE_NAME, COUNTRIES_TABLE, PORT_NUMBER, PUBLIC_SERVER_IP
from my_helpers.csv_handler import update_table
from my_helpers.database import Database

import logging

my_db = Database(DATABASE_NAME)


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--https':
            run_http()

    # if --https is sent as argument main() stops here

    update()


def update():
    from my_helpers.date_handler import is_outdated
    logging.info("Upating..." if is_outdated() else "Up to date")
    if is_outdated():
        my_db.update_table(COUNTRIES_TABLE)
        update_table()  # csv table
        set_date_to_cache()


def run_http():
    from my_helpers.http_handler import SimpleHTTPRequestHandler
    httpd = HTTPServer((PUBLIC_SERVER_IP, PORT_NUMBER), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
