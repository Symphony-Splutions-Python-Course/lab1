from http.server import HTTPServer, BaseHTTPRequestHandler
from lab1.Maki.utils.constants import *

from lab1.Maki.utils.scrape import *
from json import dumps



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        from lab1.Maki.first_project import update
        self.send_response(200)

        self.send_header('last-modified', format_date(get_last_date()))
        self.send_header('content-type', "application/json")
        self.end_headers()

        update()
        try:
            self.wfile.write(str_to_bin(get_stats()))
        except BrokenPipeError:
            print(BrokenPipeError.args)





def str_to_bin(string):
    return format_to_json(ATTRIBUTE_NAMES, string)


def format_to_json(names, data):
    list_names = names.split(',')
    list_data = data.split(',')
    dict_data = dict(zip(list_names, list_data))
    return dumps(dict_data).encode()
