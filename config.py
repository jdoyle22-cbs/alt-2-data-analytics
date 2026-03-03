import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini') # Read the configuration file

    # Accessing values
    debug = config.getboolean('General', 'debug')
    genre = config.get('General', 'genre')

    return {
        'debug': debug,
        'genre': genre
    }
