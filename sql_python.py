import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    cnn = None 
    try:
        conn = sqlite3.connect(db_name)
        print('connected created')
    except Error as e:
        print('coonection cannot be created', e)