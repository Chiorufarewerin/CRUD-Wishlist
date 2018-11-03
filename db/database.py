'''Work algorithm with database.'''

from mysql import connector
import db


class Database:
    '''Database class for working with database'''

    def __init__(self, config):
        pass

    def connect(self):
        '''Connecting with database, else ask user for reconnect.'''

    def disconnect(self):
        '''Disconnect from database.'''

    def run_query(self, query, values=None):
        '''Run query and fetch data'''
