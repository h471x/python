from classes.dbconfig import DatabaseConfigurator as dbConfig
from classes.dbquery import DatabaseQuery as dbQuery

from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

def initTables():
    tables = abs(jn(dir(__file__), 'tables.sql'))
    with open(tables, 'r') as postgresTables:
        createQuery = postgresTables.read()

    dbQuery().execute(createQuery)

def getStatus():
    return dbConfig().getStatus()

if __name__ == '__main__':
    getStatus()
    initTables()
