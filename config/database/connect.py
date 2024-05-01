from classes.dbconfig import DatabaseConfigurator as dbConfig

def getConnection():
    return dbConfig().getConnection()

def getStatus():
    return dbConfig().getStatus()

if __name__ == '__main__':
    getConnection()
    getStatus()
