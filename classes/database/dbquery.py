from .dbconfig import DatabaseConfigurator as dbConfig

class DatabaseQuery:
    def __init__(self):
        self.db = dbConfig()
        self.postgres = self.db.postgres

    def execute(self, query):
        try:
            connection = self.db.getConnection()
            cursor = connection.cursor()
            cursor.execute(query)
            queryHasReturnValue = cursor.description is not None

            if queryHasReturnValue:
                return cursor.fetchall()
            else:
                print("Query executed successfully.")
            return True
        except self.postgres.Error as e:
            print("Cannot execute the query")
            print("Error executing query:", e)
