from TravelersBoard import constants
from TravelersBoard.settings import *

DEPLOYMENT_LEVEL = constants.TEST

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travelers_board_test_db',
        'USER': 'root',
        'PASSWORD': 'dlwlehd12',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
