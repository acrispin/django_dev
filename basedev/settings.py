"""
Django settings for basedev project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*zcv1@+4oq^_kqdtce+e-qty!z6_576k*3eda0=!-%#v)qx%+o'

# SECURITY WARNING: don't run with debug turned on in production!
"""
!!!! NO OLVIDAR QUE AL DEPLOYAR EN HEROKU SETEAR LOS VALORES DE SETTINGS.PY A:
    DEBUG = False
    DEPLOY_HEROKU = True

!!!! EN DESARROLLO
    DEBUG = True
    DEPLOY_HEROKU = False
"""
DEBUG = False
DEPLOY_HEROKU = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'apprest',
    'main',
    'polls',
    'app.raw',
    # 'easy_pdf',
)

## descomentar el siguiente bloque para hacer el api rest con autenticacion
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'basedev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

if DEPLOY_HEROKU:
    WSGI_APPLICATION = 'basedev.wsgi_prd.application'
else:
    WSGI_APPLICATION = 'basedev.wsgi_dev.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'restdb',
        'USER': 'postgres',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es_es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True



UPLOAD_DIRS = os.path.join(BASE_DIR,  'files')



#################################################################################### HEROKU
if DEPLOY_HEROKU:
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

#http://stackoverflow.com/questions/19891454/static-files-in-django-1-6
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# if not DEPLOY_HEROKU:
#     # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
#     STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
## https://devcenter.heroku.com/articles/django-assets
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# para poner cache a los js cargados con requirejs
SYS_VERSION = '1234ABCD'


## para deshabilitar el logging
if not DEBUG:
    LOGGING_CONFIG = None

LOGFILE_NAME = os.path.join(BASE_DIR,  'logs/app.log')
# Max size allowed for one file
# This setting will be used by 'RotatingFileHandler'
# I have kept maxBytes to low value.
# Just for demonstration purpose.
LOGFILE_SIZE = 100*1024 # 1 * 1024 * 1024 # bytes
# Log file count
LOGFILE_COUNT = 10

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'verboseFull': {
            'format': '%(levelname)s %(asctime)s %(module)s %(pathname)s %(name)s %(filename)s %(funcName)s %(lineno)d %(msecs)d %(message)s'
        },
        'verboseOK': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] - %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },        
        'file': {
            'level': 'DEBUG',
            'formatter': 'verboseOK',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE_NAME,
            'maxBytes': LOGFILE_SIZE,
            'backupCount': LOGFILE_COUNT,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'apprest': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'main': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'polls': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# import logging.config
# logging.config.dictConfig(LOGGING)

## info logging: 
## http://www.webforefront.com/django/setupdjangologging.html 
## https://docs.djangoproject.com/en/1.8/topics/logging/