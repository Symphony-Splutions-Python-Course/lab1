
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

COUNTRIES_TABLE = "countries"

my_db = None
