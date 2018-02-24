from configurations import values

from .base import BaseConfiguration


class Local(BaseConfiguration):

    DEBUG = values.Value(environ_prefix=None, default=True)
