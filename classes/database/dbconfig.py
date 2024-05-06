import os
from configparser import ConfigParser

import psycopg2 as postgres
from psycopg2 import DatabaseError as dbError

from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..' '..')))

from classes.utils.filecreator import FileGenerator as newFile

iniFile = '../../config/database/postgres.ini'

class DatabaseConfigurator:
    def __init__(self):
        self.postgres = postgres
        self.iniFile = iniFile
        self.section = 'postgresql'

    def __getIniFile(self):
        iniDir = os.path.dirname(os.path.abspath(__file__))
        dbConfigPath = os.path.join(iniDir, self.iniFile)

        if not os.path.exists(dbConfigPath):
            raise FileNotFoundError(f"Configuration file '{self.iniFile}' not found.")
        return dbConfigPath

    def loadDbConfig(self):
        parser = ConfigParser()
        parser.read(self.__getIniFile())

        dbConfig = {}
        if parser.has_section(self.section):
            params = parser.items(self.section)
            for param in params:
                dbConfig[param[0]] = param[1]
        else:
            raise Exception(f"Section '{self.section}' not found in the '{self.filename}' file.")
        return dbConfig

    def getConnection(self):
        try:
            dbConfig = self.loadDbConfig()
            connection = self.postgres.connect(**dbConfig)
            connection.autocommit = True
            return connection
        except (dbError, Exception) as error:
            print(error)
            print("Disconnected from the PostgreSQL Database.")
            return None

    def closeConnection(self):
        self.getConnection().close()

    def getStatus(self):
        connection = self.getConnection()
        if connection:
            self.closeConnection()
            return 'connected'
        else:
            return None

    def getTableInfos(self, createQuery):
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

    def createClassFile(self, createQuery):
        table = self.getTableInfos(createQuery)
        tableClass = newFile('classes/tables')

        for tableName, attributes in table.items():
            table_name_lower = tableName.lower()
            class_file_name = f"{table_name_lower}.py"
            file_path = tableClass.getFilePath(class_file_name)

            # Check if the file exists and is blank (size is 0)
            if not os.path.exists(file_path) or (os.path.exists(file_path) and os.path.getsize(file_path) == 0):
                # Get the attributes
                table_attributes = {attr for attr in attributes}

                # Generate default data dictionary with multi-line formatting
                # Add 8 identations = 32 spaces after each line break
                default_data = ",\n".join([f"'{attr}': '{attr}'" for attr in attributes])
                default_data = default_data.replace('\n', '\n' + ' ' * 32)

                # Generate default newData
                default_new_data = ",\n".join([f"'{attr}': 'new_{attr}'" for attr in attributes])
                default_new_data = default_new_data.replace('\n', '\n' + ' ' * 32)

                tableClassContent = (
                    f"""from sys import path
                    from os.path import abspath as abs, join as jn, dirname as dir
                    path.append(abs(jn(dir(__file__), '..', '..')))

                    from classes.database.dbcrud import CrudHandler as handleCrud

                    class {tableName}_Controller:
                        def __init__(self):
                            self.__{table_name_lower} = handleCrud('{tableName}')
                            self.__attributes = {table_attributes}
                            self.__default_data = {{
                                {default_data}
                            }}
                            self.__default_new_data = {{
                                {default_new_data}
                            }}

                        def insert(self, {table_name_lower}_data):
                            self.__{table_name_lower}.insert(
                                {table_name_lower}_data
                            )
                    """
                )

                # Adjust indentation for subsequent lines
                # Remove 4 indentations = 4 x 4 spaces = 16 spaces
                identations = 5
                lines = tableClassContent.split('\n')
                adjusted_lines = [lines[0]] + [line[identations*4:] for line in lines[1:]]
                tableClassContent = '\n'.join(adjusted_lines)

                tableClass.writeFile(file_path, tableClassContent)

                # print(f"{tableName} {{ {', '.join(attributes)} }}")
                print(f"New Class File  : classes/tables/{class_file_name}")
            else:
                # print(f"{class_file_name} already exists")
                pass

    def createControllerFile(self, createQuery):
        table = self.getTableInfos(createQuery)
        tableClass = newFile('app/controllers')

        for tableName, attributes in table.items():
            table_name_lower = tableName.lower()
            class_file_name = f"{table_name_lower}.py"
            file_path = tableClass.getFilePath(class_file_name)

            # Check if the file exists and is blank (size is 0)
            if not os.path.exists(file_path) or (os.path.exists(file_path) and os.path.getsize(file_path) == 0):
                # Get the attributes
                table_attributes = {attr for attr in attributes}

                # Generate default data dictionary with multi-line formatting
                # Add 6 identations = 24 spaces after each line break
                default_data = ",\n".join([f"'{attr}': '{attr}'" for attr in attributes])
                default_data = default_data.replace('\n', '\n' + ' ' * 24)

                # Generate default newData
                default_new_data = ",\n".join([f"'{attr}': 'new_{attr}'" for attr in attributes])
                default_new_data = default_new_data.replace('\n', '\n' + ' ' * 24)

                tableControllerContent = (
                    f"""from sys import path
                    from os.path import abspath as abs, join as jn, dirname as dir
                    path.append(abs(jn(dir(__file__), '..', '..')))

                    from classes.tables.{table_name_lower} import {tableName}_Controller as {table_name_lower}

                    {table_name_lower}_data = {{
                        {default_data}
                    }}

                    {table_name_lower}_new_data = {{
                        {default_new_data}
                    }}

                    {table_name_lower} = {table_name_lower}()

                    def insert_template():
                        {table_name_lower}.insert({table_name_lower}_data)

                    """
                )

                # Adjust indentation for subsequent lines
                # Remove 4 indentations = 4 x 4 spaces = 16 spaces
                identations = 5
                lines = tableControllerContent.split('\n')
                adjusted_lines = [lines[0]] + [line[identations*4:] for line in lines[1:]]
                tableControllerContent = '\n'.join(adjusted_lines)

                tableClass.writeFile(file_path, tableControllerContent)

                # print(f"{tableName} {{ {', '.join(attributes)} }}")
                print(f"New Controller File  : app/controllers/{class_file_name}")
            else:
                # print(f"{class_file_name} already exists")
                pass
