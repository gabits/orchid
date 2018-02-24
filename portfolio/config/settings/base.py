import os
import sys

from os.path import join
from environ import Path
from configurations import Configuration, values


class BaseConfiguration(Configuration):

    DJANGO_SETTINGS_MODULE = 'config.settings'

    PROJECT_NAME = 'Portfolio'

    BASE_DIR = Path(__file__) - 3           # orchid/portfolio/config/settings/base.py - 3 = orchid/portfolio/
    ROOT_URLCONF = 'config.urls'
    WSGI_APPLICATION = 'config.wsgi.application'

    # TODO: make secret key an environment variable
    SECRET_KEY = values.Value(environ_prefix=None, default='LOCAL')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.Value(environ_prefix=None, default=False)
    ALLOWED_HOSTS = values.ListValue(['*'])

    DJANGO_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    CUSTOM_APPS = [
        # Project apps by dependency chain
        'works',
        'gallery',
        'works',
    ]

    INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS


    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [(BASE_DIR + 'templates/'),
                     (BASE_DIR + 'common/templates/')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    # Data storage
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'orchid',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


    # Password validation
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


    # Internationalisation
    LANGUAGE_CODE = 'en-gb'
    USE_I18N = True
    USE_L10N = True
    TIME_ZONE = 'UTC'
    USE_TZ = True


    # Static files
    STATIC_URL = '/static/'
    # TODO: understand how to do it through django-environ instead of stringifying
    STATICFILES_DIRS = [
        join(str(BASE_DIR), 'static'),
    ]
