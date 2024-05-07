from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

class APP_USER_Controller:
    def __init__(self):
        self.__app_user = handleCrud('APP_USER')
        self.__attributes = {'password', 'username'}
        self.__default_data = {
            'username': 'username',
            'password': 'password'
        }
        self.__default_new_data = {
            'username': 'new_username',
            'password': 'new_password'
        }

    def insert(self, app_user_data):
        self.__app_user.insert(
            app_user_data
        )

    def selectAll(self, app_user_data):
        return self.__app_user.selectAll()
