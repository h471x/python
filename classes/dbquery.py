from .dbconfig import DatabaseConfigurator as dbConfig

class DatabaseQuery:
    def __init__(self):
        __db = dbConfig()
        self.connection = __db.getConnection()
        self.postgres = __db.postgres

    def execute(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            queryHasReturnValue = cursor.description is not None

            if queryHasReturnValue:
                return cursor.fetchall()
            else:
                print("Query executed successfully.")
        except self.postgres.Error as e:
            print("Cannot execute the query")
            print("Error executing query:", e)
