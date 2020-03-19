import configparser
import os
import sys

parser = configparser.ConfigParser()
try:
    filename = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "utils/", "configs.ini")
    print(filename)
    with open(filename, 'r') as configfile:
        try:
            parser.read(filename)
        except configparser.MissingSectionHeaderError:
            print("No header")
except FileNotFoundError:
    print("File not found")
    exec(open(os.path.abspath("configs.ini")).read())
    exit(1)
print(parser.sections())
for key in parser.keys():
    print(key)
ATTRIBUTE_NAMES = parser['file']['att_names']
ATTRIBUTE_NAMES_DB = parser["DB"]['att_names_db']
URL = parser["HTTP"]['URL']
LOCAL_SERVER_IP = parser["HTTP"]['local_server_ip']
PUBLIC_SERVER_IP = parser["HTTP"]['public_server_ip']
PORT_NUMBER = parser["HTTP"]['port_number']

CSV_FILE_NAME = parser["file"]['file_name']
DATABASE_NAME = parser["DB"]['db_name']
COVID_TABLE = parser["DB"]['stats_table']

STATS_DB_KEY = parser["mc_keys"]['stats_db_key']
STATS_KEY = parser["mc_keys"]['stats_key']
DATE_KEY = parser["mc_keys"]['date_key']
HEADER_KEY = parser["mc_keys"]['header_key']
DATABASE_KEY = parser["mc_keys"]['database_key']

COUNTRIES_TABLE = parser["DB"]['countries_table']
