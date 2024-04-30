import psycopg2 as postgres
from psycopg2 import DatabaseError as dbError
from .database import loadDbConfig

def init(dbConfig):
    status = 'disconnected'
    try:
        with postgres.connect(**dbConfig) as conn:
            # print('Connected to the PostgreSQL server.')
            status = 'connected'
            return conn, status
    except (dbError, Exception) as error:
        print(error)
        print('Disonnected from the PostgreSQL server.')
        return None, status

def connect():
    dbConfig = loadDbConfig()
    return init(dbConfig)

if __name__ == '__main__':
    connect()
