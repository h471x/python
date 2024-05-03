from .dbquery import DatabaseQuery as dbQuery

class CrudHandler():
    def __init__(self, table):
        self.db = dbQuery()
        self.table = table

    def __getColumn(self, data):
        return ', '.join(data.keys())

    def __getValues(self, data):
        return ', '.join([f"'{value}'" for value in data.values()])

    def insert(self, data):
        insertQuery = f"""
            INSERT INTO {self.table} ({self.__getColumn(data)})
            VALUES ({self.__getValues(data)});
        """
        self.db.execute(insertQuery)
