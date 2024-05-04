from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.dbcrud import CrudHandler as handleCrud

user = handleCrud('APP_USER')

userData = {
    'username': 'python',
    'password': 'python'
}

newUserData = {
    'username': 'python2',
    'password': 'python2'
}

# insert user
# user.insert(userData)

# select all users
users = user.selectAll()
print(users)

# select specified user
specUser = user.select(userData)
print(specUser)

# update user
# user.update(userData, newUserData)

# delete all users
# user.deleteAll()

# delete specified user
# user.delete(userData)
