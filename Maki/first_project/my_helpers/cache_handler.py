import memcache

from my_helpers.constants import LOCAL_SERVER_IP, STATS_KEY, STATS_DB_KEY, DATE_KEY
from datetime import datetime

CACHE = memcache.Client(LOCAL_SERVER_IP)


def set_date_to_cache(date=datetime.now()):
    CACHE.set(DATE_KEY, date)


def set_stats_to_cache(content):
    CACHE.set(STATS_KEY, content)


def set_table_to_cache(content, table_name):
    CACHE.set(table_name, content)


def get_last_date():
    return CACHE.get(DATE_KEY)


def get_table_cache(table_name):
    return CACHE.get(table_name)


def get_stats_from_cache(db=False):
    return CACHE.get(STATS_DB_KEY) if db else CACHE.get(STATS_KEY)
