import sqlite3 as sql
from my_helpers.scrape import get_table, DATABASE_NAME
from my_helpers.date_handler import *
import logging

class Database:
    # how to make Database inherit and also put new fields. sql.connection is written in C
    def __init__(self, db_name):
        self.tables = dict()
        self.last_row = None
        self.connection = sql.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, command, values=None):
        logging.debug(command)
        if values is None:
            self.cursor.execute(command)
            self.commit()
            return
        self.cursor.execute(command, values)
        self.connection.commit()

    def commit(self):
        self.connection.commit()

    def add_row_input(self):
       pass

    def add_row(self, values, table_name):
        table_name = table_name.strip()
        try:
            self.execute("INSERT INTO " + table_name + " VALUES(" + values + ")")
            self.commit()
        except sql.IntegrityError:
            logging.error("IntegrityError. On INSERT. Most likely Unique constraint violation")

    def create_table_input(self):
        table_name = input("Enter table name: ")
        attributes = self.input_table()
        self.execute("CREATE TABLE " + input("Enter table name: ") + "(" + attributes + ")")
        self.tables[table_name] = attributes
        self.commit()

    def create_table(self, table_name, att):
        try:
            self.execute("CREATE TABLE " + table_name.strip() + "(" + att.strip() + ")")
        except sql.OperationalError:
            logging.error("Table exists")

    def show_tables(self):
        print(self.tables)

    def read_all(self):
        return self.execute("SELECT * FROM " + DATABASE_NAME)

    def update(self, stats, table):
        self.add_row(stats, table_name=table)

    @staticmethod
    def print(result):
        for row in result:
            print(row)

    def select(self, attributes, table_name, conditions=""):
        if attributes.strip() == 0:
            logging.warning("Nothing entered for table")
            return None

        if len(conditions.strip()) == 0:
            self.execute("SELECT " + attributes + " FROM " + table_name)
        else:
            self.execute("SELECT " + attributes + " FROM " + table_name + " WHERE " + conditions)
        return self.cursor.fetchall()

    def select_input(self):
        attributes = input("Select attributes: ")
        table_name = input("From table: ")
        conditions = input("Where(Leave empty to skip): ")
        self.select(attributes, table_name, conditions)

        # TODO: set number of attributes according to the number of columns in the table

    def input_row(self, table_name):
        new_row = list()
        for att in self.tables[table_name]:
            new_row.append(input("Enter value for" + att + ": ").strip())
        return str.join(",", new_row)

    @staticmethod
    def input_table():
        n = input("Enter number of attributes: ")
        l = []
        for i in range(n):
            att = input("Enter attribute name: ")
            att_type = input("Enter attribute type: ")
            l.append(att + " " + att_type)
        return str.join(",", l)

    def print_table(self, table_name):
        for row in (self.select("*", table_name=table_name)):
            print(row)

    def update_table(self, table_name):
        names, rows = get_table()
        self.create_table(table_name, names)
        if is_outdated():
            for row in rows:
                self.add_row(row, table_name)
