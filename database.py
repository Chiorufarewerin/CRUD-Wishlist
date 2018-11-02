'''Work algorithm with database.'''

from mysql import connector # pylint: disable=unused-import
from database_config import CONFIGDB, QUERYES # pylint: disable=unused-import

class Database:
    '''Database class for working with database'''
    def __init__(self, config):
        pass
    def connect(self):
        '''Connecting with database, else ask user for reconnect.'''

    def disconnect(self):
        '''Disconnect from database.'''

    def _runquery(self, query, values=None):
        '''Run query and fetch data'''
