from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

app_student = handleCrud('APP_STUDENT')

app_student_data_template = {
    'username': 'username',
    'password': 'password',
    'cursus': 'cursus',
    'class': 'class'
}

app_student_new_data_template = {
    'username': 'new_username',
    'password': 'new_password',
    'cursus': 'new_cursus',
    'class': 'new_class'
}

def app_student_insert_template():
    app_student.insert(app_student_data_template)

def app_student_insert(app_student_data):
    app_student.insert(app_student_data)

def app_student_selectAll():
    return app_student.selectAll()

def app_student_count():
    return app_student.count()

def app_student_select(app_student_data):
    return app_student.select(app_student_data)

def app_student_update(app_student_data, app_student_new_data):
    app_student.update(app_student_data, app_student_new_data)

def app_student_delete(app_student_data):
    app_student.delete(app_student_data)

def app_student_deleteAll():
    app_student.deleteAll()

if __name__ == '__main__':
    print("insert template")
    app_student_insert_template()
    print(app_student_selectAll())
    print(" ")

    print("select app_student_data")
    print(app_student_select(app_student_data_template))
    print(" ")

    print("update app_student_data")
    app_student_update(
        app_student_data_template,
        app_student_new_data_template
    )
    print(app_student_selectAll())
    print(" ")

    print("insert app_student_data")
    app_student_insert(app_student_data_template)
    print(app_student_selectAll())
    print(" ")

    print("Counting app_student")
    print(f"Number of app_student : {app_student_count()}")
    print(" ")

    print("delete app_student_data")
    app_student_delete(app_student_data_template)
    print(app_student_selectAll())
    print(" ")

    print("delete all")
    app_student_deleteAll()
    print(app_student_selectAll())
