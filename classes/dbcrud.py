from .dbquery import DatabaseQuery as dbQuery

class CrudHandler():
    def __init__(self, table):
        self.db = dbQuery()
        self.table = table

    def __getColumn(self, data):
        return ', '.join(
            data.keys()
        )

    def __getValues(self, data):
        return ', '.join(
            [f"'{value}'" for value in data.values()]
        )

    def __getCondition(self, condition):
        return " AND ".join(
            [f"{key} = '{value}'" for key, value in condition.items()]
        )

    def insert(self, data):
        self.db.execute(f"""
            INSERT INTO {self.table} ({self.__getColumn(data)})
            VALUES ({self.__getValues(data)});
        """)

    def selectAll(self):
        return self.db.execute(f"""
            SELECT * from {self.table};
        """)

    def select(self, condition):
        return self.db.execute(f"""
            SELECT * FROM {self.table}
            WHERE {self.__getCondition(condition)};
        """)

    def deleteAll(self):
        self.db.execute(f"""
            DELETE from {self.table};
        """)

    def delete(self, condition):
        self.db.execute(f"""
            DELETE FROM {self.table}
            WHERE {self.__getCondition(condition)};
        """)
