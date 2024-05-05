from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

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
user.insert(userData)

# select all users
users = user.selectAll()
print(users)

# select specified user
specUser = user.select(userData)
# print(specUser)

# insert with a raw SQL Query
rawInsertQuery = """
    INSERT INTO APP_USER (username, password)
    SELECT 'python', 'python'
    WHERE NOT EXISTS(
        SELECT 1 FROM APP_USER
        WHERE username = 'python'
    );
"""
user.rawExecute(rawInsertQuery)

# select with a raw SQL Query
rawGetQuery = "SELECT * FROM APP_USER;"
rawData = user.rawGet(rawGetQuery)

# update user
# user.update(userData, newUserData)

# delete all users
# user.deleteAll()

# delete specified user
# user.delete(userData)

def getData(tupleData):
    for i, dataTuple in enumerate(tupleData, 1):
        username = dataTuple[0]
        print(f"user{i}: {username}")

    print(f"Number of users: {len(tupleData)}")

# getData(users)
