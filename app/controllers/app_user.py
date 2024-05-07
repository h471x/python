from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

app_user = handleCrud('APP_USER')

app_user_data_template = {
    'username': 'username',
    'password': 'password'
}

app_user_new_data_template = {
    'username': 'new_username',
    'password': 'new_password'
}

def app_user_insert_template():
    app_user.insert(app_user_data_template)

def app_user_insert(app_user_data):
    if app_user.hasValidAttributes(app_user_data):
        app_user.insert(app_user_data)
    else:
        print(f"Data : {app_user_data}")
        print("Have Invalid Attributes")

def app_user_selectAll():
    return app_user.selectAll()

def app_user_select(app_user_data):
    if app_user.hasValidAttributes(app_user_data):
        return app_user.select(app_user_data)
    else:
        print(f"Query : {app_user_data}")
        print("Have Invalid Attributes")

def app_user_update(app_user_data, app_user_new_data):
    if app_user.hasValidAttributes(
        app_user_data,
        app_user_new_data
    ):
        app_user.update(
            app_user_data,
            app_user_new_data
        )
    else:
        print(f"Query : {app_user_data}")
        print("Have Invalid Attributes")

def app_user_delete(app_user_data):
    if app_user.hasValidAttributes(app_user_data):
        app_user.delete(app_user_data)
    else:
        print(f"Query : {app_user_data}")
        print("Have Invalid Attributes")

def app_user_deleteAll():
    app_user.deleteAll()

if __name__ == '__main__':
    print("insert template")
    app_user_insert_template()
    print(app_user_selectAll())
    print(" ")

    print("select user_data")
    print(app_user_select(app_user_data_template))
    print(" ")

    print("update user_data")
    app_user_update(
        app_user_data_template,
        app_user_new_data_template
    )
    print(app_user_selectAll())
    print(" ")

    print("insert user_data")
    app_user_insert(app_user_data_template)
    print(app_user_selectAll())
    print(" ")

    print("delete user_data")
    app_user_delete(app_user_data_template)
    print(app_user_selectAll())
    print(" ")

    print("delete all")
    app_user_deleteAll()
    print(app_user_selectAll())
