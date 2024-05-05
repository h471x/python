from classes.dbconfig import DatabaseConfigurator as dbConfig
from classes.dbquery import DatabaseQuery as dbQuery

from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

def getTableInfos(createQuery):
    table_infos = {}
    create_table_syntax = 'CREATE TABLE IF NOT EXISTS'
    queries = createQuery.split(';')
    for query in queries:
        if create_table_syntax in query:
            table_name = query.split(create_table_syntax)[1].split('(')[0].strip()
            attributes = query.split('(', 1)[1].split(')')[0].split(',')
            cleaned_attributes = [attr.split()[0].strip() for attr in attributes]
            table_infos[table_name] = cleaned_attributes
    return table_infos

def initTables():
    tables = abs(jn(dir(__file__), 'tables.sql'))
    with open(tables, 'r') as postgresTables:
        createQuery = postgresTables.read()

    table_infos = getTableInfos(createQuery)
    for table_name, attributes in table_infos.items():
        print(f"{table_name} {{ {', '.join(attributes)} }}")
    dbQuery().execute(createQuery)

def getStatus():
    return dbConfig().getStatus()

if __name__ == '__main__':
    getStatus()
    initTables()
