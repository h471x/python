from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.dbcrud import CrudHandler as handleCrud

class APP_USER_Controller:
    def __init__(self):
        self.__app_user = handleCrud('APP_USER')
        self.__default_data = {
            'username': 'username',
            'password': 'password'
        }
