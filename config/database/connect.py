import psycopg2
from .database import load_config

def init(config):
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def connect():
    config = load_config()
    init(config)

if __name__ == '__main__':
    connect()
