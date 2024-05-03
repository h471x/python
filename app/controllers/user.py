from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.dbcrud import CrudHandler as handleCrud

user = handleCrud('APP_USER')

userData = {
    'username': 'python',
    'password': 'python'
}

user.insert(userData)
