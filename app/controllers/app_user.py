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
    app_user.insert(app_user_data)

def app_user_selectAll():
    return app_user.selectAll()

def app_user_count():
    return app_user.count()

def app_user_select(app_user_data):
    return app_user.select(app_user_data)

def app_user_update(app_user_data, app_user_new_data):
    app_user.update(app_user_data, app_user_new_data)

def app_user_delete(app_user_data):
    app_user.delete(app_user_data)

def app_user_deleteAll():
    app_user.deleteAll()

if __name__ == '__main__':
    print("insert template")
    app_user_insert_template()
    print(app_user_selectAll())
    print(" ")

    print("select app_user_data")
    print(app_user_select(app_user_data_template))
    print(" ")

    print("update app_user_data")
    app_user_update(
        app_user_data_template,
        app_user_new_data_template
    )
    print(app_user_selectAll())
    print(" ")

    print("insert app_user_data")
    app_user_insert(app_user_data_template)
    print(app_user_selectAll())
    print(" ")

    print("Counting app_user")
    print(f"Number of app_user : {app_user_count()}")
    print(" ")

    print("delete app_user_data")
    app_user_delete(app_user_data_template)
    print(app_user_selectAll())
    print(" ")

    print("delete all")
    app_user_deleteAll()
    print(app_user_selectAll())
