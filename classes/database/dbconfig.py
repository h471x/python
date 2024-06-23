import os
from configparser import ConfigParser

import psycopg2 as postgres
from psycopg2 import DatabaseError as db_error

ini_file = '../../config/database/connection/postgres.ini'

class DatabaseConfigurator:
    def __init__(self):
        self.postgres = postgres
        self.ini_file = ini_file
        self.section = 'postgresql'

    def get_ini_file(self):
        ini_dir = os.path.dirname(os.path.abspath(__file__))
        db_config_path = os.path.join(ini_dir, self.ini_file)

        if not os.path.exists(db_config_path):
            raise FileNotFoundError(f"Configuration file '{self.ini_file}' not found.")
        return db_config_path

    def load_db_config(self):
        parser = ConfigParser()
        parser.read(self.get_ini_file())

        db_config = {}
        if parser.has_section(self.section):
            params = parser.items(self.section)
            for param in params:
                db_config[param[0]] = param[1]
        else:
            raise Exception(f"Section '{self.section}' not found in the '{self.ini_file}' file.")
        return db_config

    def get_connection(self):
        try:
            db_config = self.load_db_config()
            connection = self.postgres.connect(**db_config)
            connection.autocommit = True
            return connection
        except (db_error, Exception) as error:
            print(error)
            print("Disconnected from the PostgreSQL Database.")
            return None

    def close_connection(self):
        self.get_connection().close()

    def get_status(self):
        connection = self.get_connection()
        if connection:
            self.close_connection()
            return 'connected'
        else:
            return None
