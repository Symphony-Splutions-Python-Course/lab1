from datetime import datetime

from bs4 import BeautifulSoup
import requests
import re
from lab1.Maki.utils.constants import *
from lab1.Maki.utils.date_handler import *
from lab1.Maki.utils.cache_handler import *

content = requests.get(URL)


def main():
    get_table()


def format_table_row(row):
    pattern_row = re.compile("^(.*?)\ +(\d*)\ (.*?)\ +(.*?)\ (.*?)\ (.*?)\ (.*?)\ (.*?)\ (.*?)$")
    if pattern_row.groups < 9:
        return
    pattern_space = re.compile("^\ *\ $")
    print(row)
    groups = pattern_row.match(row)
    table_row = list()
    for i in range(3, 10):
        group = groups.group(i)
        if pattern_space.match(group):
            group = None  # TODO: None in SQL???
        table_row.append(group)
    return str.join(",", table_row)


def get_table():
    """returns a list of lists of all the table entries"""
    soup = BeautifulSoup(content.text, "html.parser")
    names = "Country_Other,TotalCase,NewCases,TotalDeaths,NewDeaths,TotalRecovered" \
            ",ActiveCase,Serious_Critical,Tot_Cases_per_1M pop"
    all_stats = list()
    for row in soup.find_all('tr'):
        row_soup = row.find_all('td')
        row_stats = list()
        for entry in row_soup:
            row_entry = entry.text.strip().replace("+", "").replace(",", "").replace(" ", "_")
            if len(row_entry) == 0:
                row_entry = "0"  # TODO: NULL type for sql
            if not row_entry.replace('.','',1).isdigit(): # check if it is not a number
                row_entry = ("\"" + row_entry + "\"")
            row_stats.append(row_entry)
        if row_stats == [] or row_stats[0] == "Total:":
            continue
        print(str.join(",", row_stats))
        all_stats.append(str.join(",", row_stats))
    return names, all_stats


def get_content():
    last_date = get_last_date()
    
    if last_date is None or is_outdated(last_date):
        print("Content updated. 5 minutes have passed since last cache")
        last_date = set_date_to_cache()
        set_stats_to_cache(get_stats())

    print("Seconds passed since last update: " + str(diff_in_seconds()) + "s")
    content_html = CACHE.get(STATS_KEY)

    if content_html is None:
        content_html = requests.get(URL)

    return content_html


def get_stats():
    content = get_content()
    soup = BeautifulSoup(content.text, "html.parser")
    table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
    table_stats[0] = str(format_date(get_last_date()) + "h")
    stats_csv = str.join(",", table_stats)
    return stats_csv



if __name__ == '__main__':
    main()
