#!/usr/bin/env python
import os
import sys
from .common.scripts.get_configuration import discover_configuration


if __name__ == "__main__":
    path, cls = discover_configuration()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", path)
    os.environ.setdefault("DJANGO_CONFIGURATION", cls)

    # Get environment variables from env file
    try:
        import dotenv
        dotenv.read_dotenv()
    except ImportError:
        dotenv = None

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
