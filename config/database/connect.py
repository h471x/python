import psycopg2 as pg
from psycopg2 import DatabaseError as dbError
from .database import loadConfig

def init(config):
    status = 'disconnected'
    try:
        with pg.connect(**config) as conn:
            # print('Connected to the PostgreSQL server.')
            status = 'connected'
            return conn, status
    except (dbError, Exception) as error:
        print(error)
        return None, status

def connect():
    config = loadConfig()
    return init(config)

if __name__ == '__main__':
    connect()
