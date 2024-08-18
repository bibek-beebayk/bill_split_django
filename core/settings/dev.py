from .base import BASE_DIR

SECRET_KEY = "django-insecure-@q_)0v_g0gmv%suw3($e0bp+1j=myhbq)@_ad@o!09r3d9keo_"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MEDIA_URL =  'media/'
MEDIA_ROOT =  BASE_DIR / 'media'

CSRF_ALLOW_ALL_ORIGINS = True

API_BASE = "http://localhost:8000/api/v1"

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
        },
    },
    'loggers': {
        '': { # empty string
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3', # This is where you put the name of the db file. 
                 # If one doesn't exist, it will be created at migration time.
    }
}