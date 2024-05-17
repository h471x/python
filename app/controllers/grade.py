from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

grade = handleCrud('grade')

grade_data_template = {
    '--': '--',
    '--': '--',
    '--': '--',
    '--': '--'
}

grade_new_data_template = {
    '--': 'new_--',
    '--': 'new_--',
    '--': 'new_--',
    '--': 'new_--'
}

def grade_insert_template():
    grade.insert(grade_data_template)

def grade_insert(grade_data):
    grade.insert(grade_data)

def grade_selectAll():
    return grade.selectAll()

def grade_count():
    return grade.count()

def grade_select(grade_data):
    return grade.select(grade_data)

def grade_update(grade_data, grade_new_data):
    grade.update(grade_data, grade_new_data)

def grade_delete(grade_data):
    grade.delete(grade_data)

def grade_deleteAll():
    grade.deleteAll()

if __name__ == '__main__':
    print("insert template")
    grade_insert_template()
    print(grade_selectAll())
    print(" ")

    print("select grade_data")
    print(grade_select(grade_data_template))
    print(" ")

    print("update grade_data")
    grade_update(
        grade_data_template,
        grade_new_data_template
    )
    print(grade_selectAll())
    print(" ")

    print("insert grade_data")
    grade_insert(grade_data_template)
    print(grade_selectAll())
    print(" ")

    print("Counting grade")
    print(f"Number of grade : {grade_count()}")
    print(" ")

    print("delete grade_data")
    grade_delete(grade_data_template)
    print(grade_selectAll())
    print(" ")

    print("delete all")
    grade_deleteAll()
    print(grade_selectAll())
