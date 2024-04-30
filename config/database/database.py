import os
from configparser import ConfigParser

def loadConfig(filename='postgre.ini', section='postgresql'):
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to postgre.ini in the config directory
    config_path = os.path.join(script_dir, filename)

    parser = ConfigParser()
    parser.read(config_path)

    # Get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config

if __name__ == '__main__':
    config = loadConfig()
    print(config)
