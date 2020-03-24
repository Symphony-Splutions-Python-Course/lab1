from datetime import datetime
from utils.cache_handler import get_last_date


def now():
    datetime.now()


def format_date(date=datetime.now()):
    if date is None:
        return "NULL"
    return date.strftime("%b %d %Y %H")


def diff_in_seconds(date1=get_last_date(), date2=datetime.now()):
    return abs((date1.second - date2.second))


def format_minutes(date):
    str1 = date.strftime("%b %d %Y %H:")
    minutes = str((int(date.strftime("%M"))//5) * 5)
    return str1 + minutes


def is_outdated(date=get_last_date(), date2=datetime.now()):
    if date is None:
        return True
    if diff_in_seconds(date, date2) > 300:
        return True
    return False
