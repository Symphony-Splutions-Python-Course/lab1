from datetime import datetime

from bs4 import BeautifulSoup
import requests
import re
from my_helpers.constants import *
from my_helpers.date_handler import *
from my_helpers.cache_handler import *
import logging


def format_table_row(row):
    pattern_row = re.compile("^(.*?)\ +(\d*)\ (.*?)\ +(.*?)\ (.*?)\ (.*?)\ (.*?)\ (.*?)\ (.*?)$")
    if pattern_row.groups < 9:
        return
    pattern_space = re.compile("^\ *\ $")
    logging.debug(row)
    groups = pattern_row.match(row)
    table_row = list()
    for i in range(3, 10):
        group = groups.group(i)
        if pattern_space.match(group):
            group = """"NULL"""
        table_row.append(group)
    return str.join(",", table_row)


def get_table():
    """returns a list of lists of all the table entries"""
    content = get_content()
    soup = BeautifulSoup(content.text, "html.parser")
    names = "Country_Other,TotalCase,NewCases,TotalDeaths,NewDeaths,TotalRecovered" \
            ",ActiveCase,Serious_Critical,Tot_Cases_per_1_pop,Tot_Deaths_per_1_pop,Last_Updated,PRIMARY KEY(Country_Other, Last_Updated)"
    all_stats = list()
    for row in soup.find_all('tr'):
        row_soup = row.find_all('td')
        row_stats = list()
        for entry in row_soup:
            row_entry = entry.text.strip().replace("+", "").replace(",", "").replace(" ", "_")
            if len(row_entry) == 0:
                row_entry = "NULL"  # TODO: NULL type for sql
            if not row_entry.replace('.', '', 1).isdigit():  # check if it is not a number
                row_entry = ("\"" + row_entry + "\"")
            row_stats.append(row_entry)
        if not row_stats:
            continue
        if row_stats[0].strip() == "\"Total:\"":
            break
        row_stats.append("\"" + str(format_minutes(datetime.now())) + "\"")
        print(row_stats)
        all_stats.append(str.join(",", row_stats))
    return names, all_stats


def get_content():
    return requests.get(URL)


def get_stats():
    if get_stats_from_cache() is None or is_outdated():
        content = get_content()
        soup = BeautifulSoup(content.text, "html.parser")
        table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()
        table_stats[0] = str(format_date(get_last_date()) + "h")
        stats_csv = str.join(",", table_stats)
        set_stats_to_cache(stats_csv)
    return get_stats_from_cache()
