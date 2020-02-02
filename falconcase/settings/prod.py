from .base import *
import logging
#from boto3.session import Session
#from empadigital.secrets import *

DEBUG = False

SERVER_ = ''

#ALLOWED_HOSTS = ["api.empadigital.empacloud.com"]

# logger config #
#boto3_session = Session(
#  aws_access_key_id=AWS_ACCESS_KEY_ID,
#  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#  region_name=AWS_REGION_NAME
#)
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'aws': {
            'format': u"%(asctime)s [%(levelname)-8s] %(message)s [%(pathname)s:%(lineno)d]",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {
        'watchtower': {
            'level': 'DEBUG',
            'class': 'watchtower.CloudWatchLogHandler',
                     'boto3_session': boto3_session,
                     'log_group': "watchtower",
                     'stream_name': "django.empa_sync",
            'formatter': 'aws',
        },
    },
    'loggers': {
        'watchtower-logger': {
            'level': 'DEBUG',
            'handlers': ['watchtower'],
            'propagate': True,
        },
    },
}


use logger for logging as:

logger.info("info...")
logger.debug("for debug...")
logger.error("error...")


"""

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': POSTGRES_NAME,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': '5432'
    }
}"""