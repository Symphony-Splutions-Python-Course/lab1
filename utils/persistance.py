import sqlite3
import csv  


class PersistanceAgent(object):
    """ Persistance factory class.
    """

    __db = None
    __file = None

    __DB_FILE = "covid19.db"
    __CSV_FILE = "covid10.csv"

    # We should not be able to instantiate Agents.
    # This will be somehow shadowed later.
    # def __init__(self):
    #     super().__init__()

    @classmethod
    def get_db(cls, __db_file=__DB_FILE):
        if not cls.__db:
            cls.__db = sqlite3.connect(__db_file)
        return cls.__db
