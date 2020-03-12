import os
import sys
import time
from datetime import datetime, timedelta

import memcache
import requests
from bs4 import BeautifulSoup


def main():
    URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K" \
          "4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"
    mc = memcache.Client("127.0.0.1")
    key_c = "content"
    key_date = "date"
    last_date = mc.get(key_date)
    if last_date is None or (datetime.today()-last_date).seconds > (5 * 60):
        content = requests.get(URL)
        mc.set(key_c, content)

    content = mc.get(key_c)
    if content is None:
        content = requests.get(URL)
    file_name = "stats_covid19.csv"
    today = datetime.today().date()
    soup = BeautifulSoup(content.text, "html.parser")
    table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
    table_stats[0] = str(today)

    stats_csv = str.join(",", table_stats)

    if not os.path.exists(file_name):
        new_file(file_name, stats_csv)

    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    if len(lines) == 0:
        new_file(file_name, stats_csv)
        exit(1)

    edit_content(file_name, stats_csv, lines)
    mc.set(key_date, datetime.today())


def new_file(f_name, content):
    f = open(f_name, "w")
    print("Created new file")
    names_csv = "Date,Total Cases,New Cases,Total Deaths,New Deaths," \
                "Total Recovered,Active cases,Serious/Critical" \
                ",Total Cases per 1M"
    f.write(names_csv + "\n")
    f.write(content + "\n")
    f.close()
    exit(1)


def edit_content(file_name, stats, lines):
    f = open(file_name, "w")

    if str(datetime.today().date()) not in lines[-1]:
        print("Added entry for", datetime.today().date())
        lines.append(stats)

    elif lines[-1].strip() != stats.strip():
        print("Updated for", datetime.today().date())
        lines[-1] = stats

    f.write(str.join("", lines))
    f.close()


if __name__ == "__main__":
    main()
