'''Work algorithm with database.'''

import mysql.connector as connector
from mysql.connector.cursor import MySQLCursor
import db.queryes as QUERYES


class Database:
    '''Database class for working with database'''

    def __init__(self, config):
        self.config = config

    def connect(self):
        '''Connecting with database, else ask user for reconnect.'''
        while True:
            try:
                self.cnx = connector.connect(**self.config)
                self.cnx.autocommit = True
                self.cnx.raise_on_warnings = True
                self.cursor = MySQLCursor(self.cnx)
                if not self.check():
                    self.disconnect()
                    return
                break
            except connector.Error as ex:
                print(ex.msg)
        return

    def disconnect(self):
        '''Disconnect from database.'''
        try:
            self.cursor.close()
        finally:
            pass
        try:
            self.cnx.disconnect()
        finally:
            pass

    def _run_query(self, query: str, *values):
        '''Run query and fetch data'''
        self.cursor.execute(query, values)
        data = {}
        data['columns'] = self.cursor.column_names
        data['count'] = self.cursor.rowcount
        data['id'] = self.cursor.lastrowid
        data['rows'] = self.cursor.fetchall()
        return data

    def check(self):
        '''Check table in database'''
        data = self._run_query(QUERYES.CHECK_TABLE_EXISTS)
        if data['rows'][0][0] == 1:
            return True
        print('table not found')
        create = True
        if create:
            try:
                self._run_query(QUERYES.CREATE_TABLE_ENTRIES)
            except connector.Error as msg:
                print(msg)
                return False
        return False

    def get(self, query, *values):
        '''Get data'''
        data = self._run_query(query, *values)
        return data['rows']

    def insert(self, query, *values):
        '''Insert data and returns row id'''
        data = self._run_query(query, *values)
        return data['id']

    def update(self, query, *values):
        '''Update data and returns row id'''
        data = self._run_query(query, *values)
        return data['id']

    def delete(self, query, *values):
        '''Delete data and returns count rows'''
        data = self._run_query(query, *values)
        return data['count']
