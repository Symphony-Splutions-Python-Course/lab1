import memcache

from lab1.Maki.utils.constants import LOCAL_SERVER_IP, STATS_KEY, STATS_DB_KEY, DATE_KEY
from datetime import datetime

CACHE = memcache.Client(LOCAL_SERVER_IP)


def set_date_to_cache():
    CACHE.set(DATE_KEY, datetime.now())


def set_stats_to_cache(content):
    CACHE.set(STATS_KEY, content)


def set_table_to_cache(content, table_name):
    CACHE.set(table_name, content)


def get_last_date():
    ret = CACHE.get(DATE_KEY)
    # if ret is None:
    #     return datetime.now().replace(year=2019)
    return ret


def get_table_cache(table_name):
    return CACHE.get(table_name)


def get_stats_from_cache(db=False):
    return CACHE.get(STATS_DB_KEY) if db else CACHE.get(STATS_KEY)
