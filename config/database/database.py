import os
from configparser import ConfigParser

def loadDbConfig(filename='postgres.ini', section='postgresql'):
    # Get the directory of the .ini file
    iniDir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to postgre.ini in the config directory
    dbConfigPath = os.path.join(iniDir, filename)

    parser = ConfigParser()
    parser.read(dbConfigPath)

    # Get section, default to postgresql
    dbConfig = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            dbConfig[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return dbConfig

if __name__ == '__main__':
    dbConfig = loadDbConfig()
    print(dbConfig)
