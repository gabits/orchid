from configurations import values

from .base import BaseConfiguration


class LocalConfiguration(BaseConfiguration):

    DEBUG = values.Value(environ_prefix=None, default=True)
