from .dbquery import DatabaseQuery as db_query

class CrudHandler(db_query):
    def __init__(self, table):
        super().__init__()
        self.table = table

    def get_column(self, data):
      return ', '.join(
        data.keys()
      )

    def get_values(self, data):
      return ', '.join([
        f"'{value}'" for
        value in data.values()]
      )

    def get_first_column(self, data):
        return self.get_column(data).split(', ')[0]

    def get_first_value(self, data):
        return self.get_values(data).split(', ')[0].strip("'")

    def get_condition(self, condition):
      return " AND ".join([
        f"{key} = '{value}'" for key,
        value in condition.items()]
      )

    def get_set_values(self, new_data):
      return ", ".join([
        f"{key} = '{value}'" for key,
        value in new_data.items()]
      )

    def get_table_columns(self):
        return [
          row[0] for row in self.execute(f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE
            table_schema = 'public' AND
            table_name = '{self.table.lower()}';
          """)
        ]

    def has_valid_attributes(self, *data):
      return all(
        all(key.lower() in self.get_table_columns()
            for key in data)
        for data in data
      )

    def raw_get(self, get_query):
        return self.execute(get_query)

    def raw_execute(self, execute_query):
        self.execute(execute_query)

    def insert(self, data):
        if self.has_valid_attributes(data):
            first_column = self.get_first_column(data)
            first_value = self.get_first_value(data)

            self.execute(f"""
                INSERT INTO {self.table} ({self.get_column(data)})
                SELECT {self.get_values(data)}
                WHERE NOT EXISTS(
                    SELECT 1 FROM {self.table}
                    WHERE {first_column} = '{first_value}'
                );
            """
            )

    def select_all(self):
        return [tuple(self.get_table_columns())] + self.execute(f"""
            SELECT * FROM {self.table};"""
        )

    def count(self):
        return self.execute(f"""
            SELECT COUNT(*) FROM {self.table};
        """
        )[0][0]

    def select(self, condition):
        if self.has_valid_attributes(condition):
            return [tuple(self.get_table_columns())] + self.execute(f"""
                SELECT * FROM {self.table}
                WHERE {self.get_condition(condition)};
            """
            )

    def update(self, old_data, new_data):
        if self.has_valid_attributes(old_data, new_data):
            self.execute(f"""
                UPDATE {self.table} SET {self.get_set_values(new_data)}
                WHERE {self.get_condition(old_data)}
                AND NOT EXISTS (
                    SELECT 1 FROM {self.table}
                    WHERE {self.get_condition(new_data)}
                );
            """
            )

    def delete_all(self):
        self.execute(f"""
            DELETE from {self.table};
        """
        )

    def delete(self, condition):
        if self.has_valid_attributes(condition):
            self.execute(f"""
                DELETE FROM {self.table}
                WHERE {self.get_condition(condition)};
            """
            )
