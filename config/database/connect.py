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
            table_name_start = query.find(create_table_syntax) + len(create_table_syntax)
            table_name_end = query.find('(')
            table_name = query[table_name_start:table_name_end].strip()
            attributes_section = query[table_name_end + 1:].strip()
            attributes_list = attributes_section[:-1].split(',')
            attributes = [attr.split()[0].strip() for attr in attributes_list if "FOREIGN KEY" not in attr]
            table_infos[table_name] = attributes
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
