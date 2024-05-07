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

if __name__ == '__main__':
    app_user_insert_template()
    app_user_insert(app_user_data_template)
    print(app_user_selectAll())
