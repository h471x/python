from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.dbquery import DatabaseQuery as dbQuery

db = dbQuery()

def initTables():
    tables = abs(jn(dir(__file__), 'tables.sql'))
    with open(tables, 'r') as postgresTables:
        createQuery = postgresTables.read()

    db.execute(createQuery)

if __name__ == '__main__':
    initTables()
