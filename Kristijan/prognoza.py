#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import memcache
import json
import datetime
from bs4 import BeautifulSoup
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import lxml

URL = "https://sitel.com.mk/meteo"

file_name = "prognoza.txt"
#my_server = "0.0.0.0"
#server = "127.0.0.1"
#port = 9000
#mc = memcache.Client(server)
today_date = datetime.date.today()
weather_stats = []
listtostring = ''
string1=''
first_line = "Времето денес " + str(today_date) + " ќе биде:"


def main():
    create_file()
    is_empty = is_file_empty(file_name)
    lines = get_lines_from_file()
    if is_empty:
        write_to_file()
    elif str(today_date) not in lines[-1]:
        update_file()
    #elif len(sys.argv) > 1 and sys.argv[1] == '--http':
        #run(HTTPServer, BaseHTTPRequestHandler)
  

def scraping_stats():
    content = requests.get(URL).text
    soup = BeautifulSoup(content, "html.parser")
    weather = soup.find_all("div", class_= "grad-info-wrapper")
    for x in weather:
        weather_stats.append(x.text)
    return str(listtostring.join(weather_stats).replace("\n"," ").split())
    
    

def write_to_file():
    with open (file_name, "w+") as file:
        file.write(first_line)
        file.write(scraping_stats())

def update_file():
    with open (file_name, "a+") as file:
        file.write("\n" + first_line)
        file.write(scraping_stats())

def get_lines_from_file():
    f = open (file_name, "r")
    lines = f.readlines()
    f.close
    return lines

def is_file_empty(file_name):
    return os.path.exists(file_name) and os.stat(file_name).st_size == 0

def create_file():
    if not os.path.exists(file_name):
        f = open (file_name,"w+")
        f.close()
    else:
        pass

#class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    #def do_GET(self):
        #self.send_response(200)
        #self.end_headers()
        #update_table()
        #self.wfile.write(str_to_bin(scrape_stats(get_content())))


#def run(server_class, handler_class):
    #httpd = HTTPServer((my_server_IP, port), SimpleHTTPRequestHandler)
    #httpd.serve_forever()

if __name__ == "__main__":
    main()