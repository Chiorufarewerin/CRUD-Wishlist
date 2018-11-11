"Initialization database connection."

import db.queryes as QUERIES
from db.database import Database
from config import CONFIGDB

DB = Database(CONFIGDB)
DB.connect()
