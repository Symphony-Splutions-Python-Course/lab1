import sys
from http.server import HTTPServer

from lab1.Maki.utils.cache_handler import set_date_to_cache, get_last_date
from lab1.Maki.utils.constants import DATABASE_NAME, COUNTRIES_TABLE, PORT_NUMBER, PUBLIC_SERVER_IP
from lab1.Maki.utils.csv_handler import update_table
from lab1.Maki.utils.database import Database


my_db = Database(DATABASE_NAME)


def main():
    if get_last_date() is None:
        set_date_to_cache()

    if len(sys.argv) > 1:
        if sys.argv[1] == '--https':
            run()

    # if --https is sent as argument main() stops here
    update()


def update():
    my_db.update_table(COUNTRIES_TABLE)
    update_table()  # csv table
    set_date_to_cache()


def run():
    from lab1.Maki.utils.http_handler import SimpleHTTPRequestHandler
    httpd = HTTPServer((PUBLIC_SERVER_IP, PORT_NUMBER), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
