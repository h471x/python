from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

# import a dbquery from 2 steps above
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.dbquery import DatabaseQuery as dbQuery

db = dbQuery()

def initDbTable():
    tables = abs(jn(dir(__file__), 'tables.sql'))
    with open(tables, 'r') as postgresTables:
        createQuery = postgresTables.read()

    db.execute(createQuery)

if __name__ == '__main__':
    initDbTable()
