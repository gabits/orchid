from os import sys


def return_configuration(config):
    path = 'config.settings.' + config
    cls = config[0].upper() + config[1:]
    return path, cls

def discover_configuration():
    # TODO: Once there's a definition of where it'll run there'll be more logic to be added here and even changed.
    if 'runserver' in sys.argv:
        config = 'local'
    return return_configuration(config)