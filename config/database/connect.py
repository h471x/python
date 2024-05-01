import psycopg2 as postgres
from psycopg2 import DatabaseError as dbError
from .database import loadDbConfig as dbConfig

def getConnection():
    try:
        with postgres.connect(**dbConfig()) as connection:
            return connection
    except (dbError, Exception) as error:
        print(error)
        print('Failed to connect to the PostgreSQL server.')
        return None

def getStatus():
    if getConnection():
        return 'connected'
    else:
        return None

if __name__ == '__main__':
    getConnection()
    getStatus()
