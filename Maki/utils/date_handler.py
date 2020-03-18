from datetime import datetime
from utils.cache_handler import get_last_date


def now():
    datetime.now()


def format_date(date):
    return date.strftime("%b %d %Y %H")


def diff_in_seconds(date1=get_last_date(), date2=datetime.now()):
    return abs((date1 - date2).seconds)


def format_minutes(date):
    return date.strftime("%b %d %Y %H:%m")


def is_outdated(date=get_last_date(), date2=datetime.now()):
    if date is None:
        return True
    if diff_in_seconds(date, date2) > 300:
        return True
    return False
