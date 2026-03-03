import configparser

"""Read the configuration file"""
def read_config() -> dict[str, str | bool]:
    config = configparser.ConfigParser()
    config.read('./config.ini') # Read the configuration file

    return {
        'debug': bool(config['general']['debug']),
        'genre': str(config['general']['genre'])
    }