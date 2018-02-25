#!/usr/bin/env python
import os
import sys
import configurations

from os.path import join, dirname


if __name__ == '__main__':

    # Set default configuration to Local
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

    configurations.setup()

    # Get environment variables from .env file
    try:
        import dotenv

        env_path = join(dirname(__file__), '.env')
        dotenv.load_dotenv(env_path)
    except ImportError:
        dotenv = None


    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
