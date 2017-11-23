#!/usr/bin/env python
import os
import sys
# from .common.scripts.get_configuration import discover_configuration

#
# def return_configuration(config):
#     path = 'config.settings.' + config
#     cls = config[0].upper() + config[1:]
#     return path, cls
#
# def discover_configuration():
#     # TODO: Once there's a definition of where it'll run there'll be more logic to be added here and even changed.
#     if 'runserver' in sys.argv:
#         config = 'local'
#     return return_configuration(config)



if __name__ == "__main__":
    # path, cls = discover_configuration()
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", path)
    # os.environ.setdefault("DJANGO_CONFIGURATION", cls)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings.local')
    os.environ.setdefault("DJANGO_CONFIGURATION", 'Local')

    # # Get environment variables from env file
    # try:
    #     import dotenv
    #     dotenv.read_dotenv()
    # except ImportError:
    #     dotenv = None

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
