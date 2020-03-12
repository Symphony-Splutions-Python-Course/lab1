from os import path
from bs4 import BeautifulSoup
import requests
import memcache
from datetime import datetime
from datetime import date

today = date.today()

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K" \
      "4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"

server_IP = "127.0.0.1"

file_name = "stats_covid19.csv"

key_c = "content"
key_date = "last_datetime"

cache = memcache.Client(server_IP)


def main():
    content = get_content()

    stats_csv = scrape_stats(content)

    if not path.exists(file_name):
        new_file(stats_csv)

    # If the file was just created the program finishes here=======================

    lines = get_lines_from_file()

    if len(lines) == 0:
        new_file(stats_csv)

    # If the file was just created the program finishes here=======================

    edit_content(stats_csv, lines)


def get_lines_from_file():
    f = open(file_name, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_content():
    last_date = cache.get(key_date)

    if last_date is None or (datetime.today() - last_date).seconds > (5 * 60):
        content = requests.get(URL)
        cache.set(key_c, content)

    content = cache.get(key_c)

    if content is None:
        content = requests.get(URL)

    return content


def scrape_stats(content):
    soup = BeautifulSoup(content.text, "html.parser")
    table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
    table_stats[0] = str(today)
    stats_csv = str.join(",", table_stats)
    return stats_csv


def new_file(content):
    names_csv = "Date,Total Cases,New Cases,Total Deaths,New Deaths," \
                "Total Recovered,Active cases,Serious/Critical" \
                ",Total Cases per 1M"

    write_to_file(content, names_csv)

    print("Created new file")
    set_date_to_mc()
    exit(1)


def edit_content(stats, lines):
    if str(today) not in lines[-1]:
        print("Added entry for", today)
        lines.append(stats + '\n')

    elif lines[-1].strip() != stats.strip():
        print("Updated for", today)
        lines[-1] = stats + '\n'

    write_to_file(lines)
    set_date_to_mc()


def set_date_to_mc():
    cache.set(key_date, datetime.today())


def write_to_file(content, names=None):
    f = open(file_name, "w")

    if names is not None:
        f.write(names + "\n")
        f.write(content + "\n")

    else:
        f.write(str.join("", content))

    f.close()


if __name__ == "__main__":
    main()
