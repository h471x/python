from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

# import login from one step above
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.dbquery import DatabaseQuery as dbQuery

db = dbQuery()

def createUserTable():
    createQuery = """
    CREATE TABLE IF NOT EXISTS app_user(
        firstname TEXT,
        lastname TEXT
    );
    """
    result = db.execute(createQuery)

def deleteUserTable():
    deleteQuery = """
    DROP TABLE IF EXISTS app_user;
    """
    result = db.execute(deleteQuery)

if __name__ == '__main__':
    # createUserTable()
    deleteUserTable()
