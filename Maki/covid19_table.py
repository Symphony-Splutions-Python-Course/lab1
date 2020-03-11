import sys
import time
import os
from bs4 import BeautifulSoup
import requests
from datetime import datetime


def main():
    URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K" \
          "4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"
    content = requests.get(URL)
    file_name = "stats_covid19.csv"

    soup = BeautifulSoup(content.text, "html.parser")
    table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
    table_stats[0] = str(datetime.today().date())

    stats_csv = str.join(",", table_stats)

    if not os.path.exists(file_name):
        new_file(file_name)

    f = open("stats_covid19.csv", "r")
    lines = f.readlines()
    f.close()

    if len(lines) == 0:
        new_file(file_name, stats_csv)
        exit(1)

    edit_content(file_name, stats_csv, lines)


def new_file(f_name, content):
    f = open("stats_covid19.csv", "w")
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

    elif lines[-1] != stats:
        print("Updated for", datetime.today().date())
        lines[-1] = stats

    f.write(str.join("", lines))
    f.close()


if __name__ == "__main__":
    main()
