import psycopg2
from psycopg2 import OperationalError

def connect_to_postgresql():
    print("Attempting to connect to the PostgreSQL database...")
    try:
        # Connection parameters
        dbname = 'postgres'
        user = 'python'
        password = 'python'
        host = 'localhost'
        port = '5432'

        # Establish connection
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

        # Create a cursor
        cursor = conn.cursor()

        # Print connection information
        print("Connected to the PostgreSQL database!")

        # Close cursor and connection
        cursor.close()
        conn.close()

    except OperationalError as e:
        print(f"Unable to connect to the PostgreSQL database: {e}")

# Call the function to connect to PostgreSQL
connect_to_postgresql()
