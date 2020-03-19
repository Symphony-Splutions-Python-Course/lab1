import sqlite3
import csv  


class DatabaseConnection(object):

    __db_connection = None
    __db_name = None

    def __init__(self, db_filename):
        super().__init__()
        self.__db_name = db_filename
        self.__db_connectopn = sqlite3.connect(db_filename)

    def __repr__(self):
        str = "Sqlite3 connection on {}".format(self.__db_name)
        return str

    def close(self):
        self.close()
        print("{} is closed now.".format(self.__db_name))


class PersistanceAgent(object):
    """ Persistance factory class.
    """

    __db_connections = {}

    __DB_FILE = "covid19.db"
    __CSV_FILE = "covid19.csv"

    # We should not be able to instantiate Agents.
    # This will be somehow shadowed later.
    # def __init__(self):
    #     super().__init__()

    @classmethod
    def get_db_connection(cls, __db_file=__DB_FILE):
        if __db_file in cls.__db_connections.keys():
            connection = cls.__db_connections[__db_file]
        else:
            connection = sqlite3.connect(__db_file)
            cls.__db_connections[__db_file] = connection
        
        return connection


    @classmethod
    def get_csv_file(cls, __filename=__CSV_FILE):
        if not cls.__file:
            cls.__file = open(__filename)
        return cls.__file

