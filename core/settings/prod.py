# Email backend
import os
from core.settings.base import BASE_DIR

SECRET_KEY = "django-insecure-@q_)0v_g0gmv%suw3($e0bp+1j=myhbq)@_ad@o!09r3d7keo_"


DEBUG = False

ALLOWED_HOSTS = []

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CSRF_TRUSTED_ORIGINS = []

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


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": site_settings.DATABASE_NAME,
#         "USER": site_settings.DATABASE_USER,
#         "PASSWORD": site_settings.DATABASE_PASSWORD,
#         "HOST": site_settings.DATABASE_HOST,
#         "PORT": site_settings.DATABASE_PORT,
#     }
# }
