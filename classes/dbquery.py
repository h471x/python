from .dbconfig import DatabaseConfigurator as dbConfig

class DatabaseQuery:
    def __init__(self):
        __db = dbConfig()
        self.connection = __db.getConnection()
        self.cursor = self.connection.cursor()
        self.postgres = __db.postgres

    def execute(self, query):
        try:
            self.cursor.execute(query)
            queryHasReturnValue = self.cursor.description is not None

            if queryHasReturnValue:
                return self.cursor.fetchall()
            else:
                print("Query executed successfully.")
        except self.postgres.Error as e:
            print("Cannot execute the query")
            print("Error executing query:", e)
