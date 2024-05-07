import os
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..' '..')))

from classes.utils.filehandler import FileHandler as newFile

class PythonGenerator:
    def getTableInfos(self, createQuery):
        table_infos = {}
        create_table_syntax = 'CREATE TABLE IF NOT EXISTS'
        queries = createQuery.split(';')
        for query in queries:
            if create_table_syntax in query:
                table_name_start = query.find(create_table_syntax) + len(create_table_syntax)
                table_name_end = query.find('(')
                table_name = query[table_name_start:table_name_end].strip()
                attributes_section = query[table_name_end + 1:].strip()
                attributes_list = attributes_section[:-1].split(',')
                attributes = [attr.split()[0].strip() for attr in attributes_list if "FOREIGN KEY" not in attr]
                table_infos[table_name] = attributes
        return table_infos

    def createControllerFile(self, createQuery):
        table = self.getTableInfos(createQuery)
        tableClass = newFile('app/controllers')

        for tableName, attributes in table.items():
            table_name_lower = tableName.lower()
            class_file_name = f"{table_name_lower}.py"
            file_path = tableClass.getFilePath(class_file_name)

            # Check if the file exists and is blank (size is 0)
            if not os.path.exists(file_path) or (os.path.exists(file_path) and os.path.getsize(file_path) == 0):
                # Get the attributes
                table_attributes = {attr for attr in attributes}

                # Generate default data dictionary with multi-line formatting
                # Add 6 identations = 24 spaces after each line break
                default_data = ",\n".join([f"'{attr}': '{attr}'" for attr in attributes])
                default_data = default_data.replace('\n', '\n' + ' ' * 24)

                # Generate default newData
                default_new_data = ",\n".join([f"'{attr}': 'new_{attr}'" for attr in attributes])
                default_new_data = default_new_data.replace('\n', '\n' + ' ' * 24)

                tableControllerContent = (
                    f"""from sys import path
                    from os.path import abspath as abs, join as jn, dirname as dir
                    path.append(abs(jn(dir(__file__), '..', '..')))

                    from classes.database.dbcrud import CrudHandler as handleCrud

                    {table_name_lower} = handleCrud('{tableName}')

                    {table_name_lower}_data = {{
                        {default_data}
                    }}

                    {table_name_lower}_new_data = {{
                        {default_new_data}
                    }}

                    def {table_name_lower}_insert_template():
                        {table_name_lower}.insert({table_name_lower}_data)

                    def {table_name_lower}_selectAll():
                        print({table_name_lower}.selectAll())

                    if __name__ == '__main__':
                        {table_name_lower}_insert_template()
                        {table_name_lower}_selectAll()
                    """
                )

                # Adjust indentation for subsequent lines
                # Remove 4 indentations = 4 x 4 spaces = 16 spaces
                identations = 5
                lines = tableControllerContent.split('\n')
                adjusted_lines = [lines[0]] + [line[identations*4:] for line in lines[1:]]
                tableControllerContent = '\n'.join(adjusted_lines)

                tableClass.writeFile(file_path, tableControllerContent)

                # print(f"{tableName} {{ {', '.join(attributes)} }}")
                print(f"New Controller File  : app/controllers/{class_file_name}")
            else:
                # print(f"{class_file_name} already exists")
                pass
