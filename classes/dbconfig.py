import os
from configparser import ConfigParser

import psycopg2 as postgres
from psycopg2 import DatabaseError as dbError

class DatabaseConfigurator:
    def __init__(self):
        self.iniFile = '../config/database/postgres.ini'
        self.section = 'postgresql'

    def loadDbConfig(self):
        # Get the directory of the .ini file
        iniDir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to postgre.ini in the config directory
        dbConfigPath = os.path.join(iniDir, self.iniFile)

        if not os.path.exists(dbConfigPath):
            raise FileNotFoundError(f"Configuration file '{self.iniFile}' not found.")

        parser = ConfigParser()
        parser.read(dbConfigPath)

        # Get section, default to postgresql
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
            with postgres.connect(**dbConfig) as connection:
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
