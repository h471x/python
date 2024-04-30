import psycopg2 as pg
from psycopg2 import DatabaseError as dbError
from .database import loadConfig

def init(config):
    try:
        with pg.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (pg.dbError, Exception) as error:
        print(error)

def connect():
    config = loadConfig()
    init(config)

if __name__ == '__main__':
    connect()
