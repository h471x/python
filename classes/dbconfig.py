import os
from configparser import ConfigParser

import psycopg2 as postgres
from psycopg2 import DatabaseError as dbError

iniFile = '../config/database/postgres.ini'

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
