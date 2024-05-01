from dbconfig import DatabaseConfigurator as dbConfig

class DatabaseQuery:
    def __init__(self):
        self.connection = dbConfig().getConnection()
        self.postgres = dbConfig().postgres

    def execute(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            queryHasReturnValue = cursor.description is not None

            if queryHasReturnValue:
                result = cursor.fetchall()
                print("Query returned values:", result)
            else:
                print("Query executed successfully.")
            return True
        except self.postgres.Error as e:
            print("Cannot execute the query")
            print("Error executing query:", e)
            return False
