from classes.database.dbconfig import DatabaseConfigurator as dbConfig
from classes.database.dbquery import DatabaseQuery as dbQuery

import os
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

def getSqlFile(sqlFile):
    return abs(jn(dir(__file__), sqlFile))

def initTables():
    with open(
        getSqlFile('tables.sql'), 'r'
    ) as postgresTables:
        createQuery = postgresTables.read()

    if dbQuery().execute(createQuery):
        dbConfig().createClassFile(createQuery)
        dbConfig().createControllerFile(createQuery)
        return True

def getStatus():
    return dbConfig().getStatus()

if __name__ == '__main__':
    getStatus()
    initTables()
