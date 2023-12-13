import sqlite3
from contextlib import closing
#from business import


DATABASE = "Final.sqlite" # Database Name

def connect():
    return sqlite3.connect(DATABASE)

def close(connection):
    connection.close()