from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

path.append(abs(jn(dir(__file__), '..', '..', '..')))

from classes.database.dbconfig import DatabaseConfigurator as db_config
from classes.database.dbquery import DatabaseQuery as db_query
from classes.utils.filegenerator import FileGenerator as create_file

def get_sql_file(sql_file):
    return abs(jn(dir(__file__), '..', 'sql', sql_file))

def init_tables():
    with open(get_sql_file('tables.sql'), 'r') as postgres_tables:
        create_query = postgres_tables.read()

    if db_query().execute(create_query):
        create_file().create_controller_file(create_query)
        return True

def load_sql_seed():
    with open(get_sql_file('seed.sql'), 'r') as data_seed:
        seed_query = data_seed.read()

    if db_query().execute(seed_query):
        return True

def get_status():
    return db_config().get_status()

if __name__ == '__main__':
    get_status()
    init_tables()
    load_sql_seed()
