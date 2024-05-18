from .dbconfig import DatabaseConfigurator as db_config

class DatabaseQuery:
    def __init__(self):
        self.db = db_config()
        self.postgres = self.db.postgres

    def execute(self, query):
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            query_has_return_value = cursor.description is not None

            if query_has_return_value:
                return cursor.fetchall()
            else:
                print("Query executed successfully.")
                return True
        except self.postgres.Error as e:
            print("Cannot execute the query")
            print("Error executing query:", e)
