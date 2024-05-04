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

    def __getFirstColumn(self, data):
        return self.__getColumn(data).split(', ')[0]

    def __getFirstValue(self, data):
        return self.__getValues(data).split(', ')[0].strip("'")

    def __getCondition(self, condition):
        return " AND ".join(
            [f"{key} = '{value}'" for key, value in condition.items()]
        )

    def __getSetValues(self, newData):
        return ", ".join(
            [f"{key} = '{value}'" for key, value in newData.items()]
        )

    def rawGet(self, getQuery):
        return self.db.execute(getQuery)

    def rawExecute(self, executeQuery):
        self.db.execute(executeQuery)

    def insert(self, data):
        __firstColumn = self.__getFirstColumn(data)
        __firstValue = self.__getFirstValue(data)
        __insert_or_ignore_query = f"""
            INSERT INTO {self.table} ({self.__getColumn(data)})
            SELECT {self.__getValues(data)}
            WHERE NOT EXISTS(
                SELECT 1 FROM {self.table}
                WHERE {__firstColumn} = '{__firstValue}'
            );
        """
        self.db.execute(__insert_or_ignore_query)

    def selectAll(self):
        return self.db.execute(f"""
            SELECT * from {self.table};
        """)

    def select(self, condition):
        return self.db.execute(f"""
            SELECT * FROM {self.table}
            WHERE {self.__getCondition(condition)};
        """)

    def update(self, oldData, newData):
        self.db.execute(f"""
            UPDATE {self.table} SET {self.__getSetValues(newData)}
            WHERE {self.__getCondition(oldData)};
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
