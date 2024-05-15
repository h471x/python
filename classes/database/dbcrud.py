from .dbquery import DatabaseQuery as dbQuery

class CrudHandler(dbQuery):
    def __init__(self, table):
        super().__init__()
        self.table = table

    def getColumn(self, data):
        return ', '.join(
            data.keys()
        )

    def getValues(self, data):
        return ', '.join([
            f"'{value}'" for
            value in data.values()]
        )

    def getFirstColumn(self, data):
        return self.getColumn(data).split(', ')[0]

    def getFirstValue(self, data):
        return self.getValues(data).split(', ')[0].strip("'")

    def getCondition(self, condition):
        return " AND ".join([
            f"{key} = '{value}'" for key,
            value in condition.items()]
        )

    def getSetValues(self, newData):
        return ", ".join([
            f"{key} = '{value}'" for key,
            value in newData.items()]
        )

    def getTableColumns(self):
        return [
            row[0] for row in self.execute(f"""
                SELECT column_name
                FROM information_schema.columns
                WHERE
                table_schema = 'public' AND
                table_name = '{self.table.lower()}';
            """
            )
        ]

    def hasValidAttributes(self, *data):
        for data in data:
            if not all(
                key in self.getTableColumns()
                for key in data
            ):
                print(f"Query : {data}")
                print("Have Invalid Attributes")
                return False
        return True

    def rawGet(self, getQuery):
        return self.execute(getQuery)

    def rawExecute(self, executeQuery):
        self.execute(executeQuery)

    def insert(self, data):
        if self.hasValidAttributes(data):
            firstColumn = self.getFirstColumn(data)
            firstValue = self.getFirstValue(data)

            self.execute(f"""
                INSERT INTO {self.table} ({self.getColumn(data)})
                SELECT {self.getValues(data)}
                WHERE NOT EXISTS(
                    SELECT 1 FROM {self.table}
                    WHERE {firstColumn} = '{firstValue}'
                );
            """
            )

    def selectAll(self):
        return self.execute(f"""
            SELECT * from {self.table};
        """
        )

    def count(self):
        return self.execute(f"""
            SELECT COUNT(*) FROM {self.table};
        """
        )[0][0]

    def select(self, condition):
        if self.hasValidAttributes(condition):
            return self.execute(f"""
                SELECT * FROM {self.table}
                WHERE {self.getCondition(condition)};
            """
            )

    def update(self, oldData, newData):
        if self.hasValidAttributes(oldData, newData):
            newFirstColumn = self.getFirstColumn(newData)
            newFirstValue = self.getFirstValue(newData)

            self.execute(f"""
                UPDATE {self.table} SET {self.getSetValues(newData)}
                WHERE {self.getCondition(oldData)}
                AND NOT EXISTS (
                    SELECT 1 FROM {self.table}
                    WHERE {newFirstColumn} = '{newFirstValue}'
                );
            """
            )

    def deleteAll(self):
        self.execute(f"""
            DELETE from {self.table};
        """
        )

    def delete(self, condition):
        if self.hasValidAttributes(condition):
            self.execute(f"""
                DELETE FROM {self.table}
                WHERE {self.getCondition(condition)};
            """
            )
