from classes.dbconfig import DatabaseConfigurator as dbConfig
from classes.dbquery import DatabaseQuery as dbQuery

import os
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

def createClass(table):
    controller_dir = abs(jn(dir(__file__), '..', '..', 'app/controllers'))
    if not os.path.exists(controller_dir):
        os.makedirs(controller_dir)

    for tableName, attributes in table.items():
        table_name_lower = tableName.lower()
        file_name = f"{table_name_lower}.py"
        file_path = jn(controller_dir, file_name)

        # Check if the file exists and is blank (size is 0)
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            tableClassContent = (
                f"""from sys import path
                from os.path import abspath as abs, join as jn, dirname as dir
                path.append(abs(jn(dir(__file__), '..', '..')))

                from classes.dbcrud import CrudHandler as handleCrud

                class {tableName}_Controller:
                    def __init__(self):
                        self.__{table_name_lower} = handleCrud('{tableName}')
                """
            )

            # Adjust indentation for subsequent lines
            # Remove 4 indentations = 4 x 4 spaces = 16 spaces
            identations = 4
            lines = tableClassContent.split('\n')
            adjusted_lines = [lines[0]] + [line[identations*4:] for line in lines[1:]]
            tableClassContent = '\n'.join(adjusted_lines)

            with open(file_path, 'w') as file:
                file.write(tableClassContent)

            print(f"{tableName} {{ {', '.join(attributes)} }}")
            print(f"File Class Generated: {file_name}")
        else:
            print(f"{file_name} aleready exists")

def initTables():
    tables = abs(jn(dir(__file__), 'tables.sql'))
    with open(tables, 'r') as postgresTables:
        createQuery = postgresTables.read()

    table_infos = getTableInfos(createQuery)
    createClass(table_infos)
    dbQuery().execute(createQuery)

def getStatus():
    return dbConfig().getStatus()

if __name__ == '__main__':
    getStatus()
    initTables()
