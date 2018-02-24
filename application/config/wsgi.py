import os

from django.core.wsgi import get_wsgi_application

from .get_configuration import discover_configuration


path, cls = discover_configuration()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", path)
os.environ.setdefault("DJANGO_CONFIGURATION", cls)

application = get_wsgi_application()
