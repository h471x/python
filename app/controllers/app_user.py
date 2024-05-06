from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.tables.app_user import APP_USER_Controller as app_user

app_user_data = {
    'username': 'username',
    'password': 'password'
}

app_user_new_data = {
    'username': 'new_username',
    'password': 'new_password'
}

app_user = app_user()

def insert_template():
    app_user.insert(app_user_data)

if __name__ == '__main__':
    insert_template()
