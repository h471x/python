import psycopg2 as pg
from psycopg2 import OperationalError as error

def pg_connect():
    try:
        # Connection parameters
        dbname = 'postgres'
        user = 'python'
        password = 'python'
        host = 'localhost'
        port = '5432'

        # Establish connection
        conn = pg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Print connection information
        print("Connected to the PostgreSQL database!")

        # Close cursor and connection
        cursor.close()
        conn.close()

    except error as e:
        print(f"Unable to connect to the PostgreSQL database: {e}")

# Call the function to connect to PostgreSQL
pg_connect()
