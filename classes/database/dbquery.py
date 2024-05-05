from .dbconfig import DatabaseConfigurator as dbConfig

class DatabaseQuery:
    def __init__(self):
        self.__db = dbConfig()
        self.postgres = self.__db.postgres

    def execute(self, query):
        try:
            connection = self.__db.getConnection()
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
