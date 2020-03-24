from utils.constants import *
from utils.date_handler import *
from utils.scrape import get_stats
from os import path
import logging


def update_table(is_request=False):
    stats = get_stats()

    if not path.exists(CSV_FILE_NAME):
        new_file(stats, is_request)

    # If the file was just created the program finishes here=======================

    lines = get_lines_from_file()

    if len(lines) == 0:
        new_file(stats, is_request)

    # If the file was just created the program finishes here=======================

    edit_content(stats, lines)


def get_lines_from_file():
    f = open(CSV_FILE_NAME, "r")
    lines = f.readlines()
    f.close()
    return lines


def new_file(content, is_request):
    write_to_file(content, ATTRIBUTE_NAMES)

    logging.info("Created new file: {}".format(format_date(get_last_date())))
    logging.debug(content)
    if not is_request:
        exit(1)


def edit_content(stats, lines):
    if format_date(get_last_date()) not in lines[-1]:
        logging.info("Added entry for {}".format(format_date(get_last_date())))
        lines.append(stats + '\n')

    elif lines[-1].strip() != stats.strip():
        logging.info("Updated for {}h".format(format_date(get_last_date())))
        lines[-1] = stats + '\n'

    else:
        logging.info("File is up to date:")
        logging.info('[', stats, ']', sep='')

    write_to_file(lines)


def write_to_file(content, names=None):
    f = open(CSV_FILE_NAME, "w")

    if names is not None:
        f.write(names + "\n")
        f.write(content + "\n")

    else:
        f.write(str.join("", content))

    f.close()
