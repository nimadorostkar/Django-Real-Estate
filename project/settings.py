import os
from pathlib import Path
from django.contrib.messages import constants as messages



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY_PLACEHOLDER'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEFAULT_LOGGING_LEVEL = "DEBUG" if DEBUG else "INFO"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'simple': {
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
            'format': '[%(asctime)s] [%(process)d] [%(levelname)s] %(name)s %(message)s',  # noqa
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
            'include_html': True
        },
        'warn_admins': {
            'level': 'WARN',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
            'include_html': True
        },
    },
    'loggers': {
        # ----------------------------------------
        # general
        # ----------------------------------------
        # make sure we have anything >= WARN whatsoever
        'root': {
            'handlers':  ["console"],
            'level': "WARN",
            'formatter': "verbose",
        },

        # ----------------------------------------
        # apps loggers - django (default)
        # ----------------------------------------
        'django': {
            'handlers':  ["console", ],
            'level': "INFO",
            'formatter': "verbose",
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

        # ----------------------------------------
        # app loggers - third part
        # ----------------------------------------
        'reportlab.platypus': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },

        # ----------------------------------------
        # app loggers - our own apps
        # ----------------------------------------
        'accounts': {
            'handlers':  ["console", ],
            'level': DEFAULT_LOGGING_LEVEL,
            'propagate': True,
        },
        'contacts': {
            'handlers':  ["console", ],
            'level': DEFAULT_LOGGING_LEVEL,
            'propagate': True,
        },
        'core': {
            'handlers':  ["console", ],
            'level': DEFAULT_LOGGING_LEVEL,
            'propagate': True,
        },
        'documents': {
            'handlers':  ["console", ],
            'level': DEFAULT_LOGGING_LEVEL,
            'propagate': True,
        },
        'listings': {
            'handlers':  ["console", ],
            'level': DEFAULT_LOGGING_LEVEL,
            'propagate': True,
        },

    }
}


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django_translation_flags',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'core.apps.CoreConfig',
    'listings.apps.ListingsConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'documents.apps.DocumentsConfig',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # for google auth

]

AUTH_USER_MODEL = 'accounts.CustomUser'

OCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

AUTHENTICATION_BACKENDS = (
    # used for default signin such as loggin into admin panel
    'django.contrib.auth.backends.ModelBackend',

    # used for social authentications
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = 'index'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crum.CurrentRequestUserMiddleware'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processor.global_variables',

            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'



# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

def gettext(s): return s


"""
    ('it', gettext('Italian')),
    ('es', gettext('Spanish')),
    ('ru', gettext('Russian')),
    ('fr', gettext('French')),
"""


LANGUAGES = (
    ('de', gettext('German')),
    ('en', gettext('English')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
   BASE_DIR / 'project/static',
]

print(BASE_DIR / 'project/static')
# Media Folder Settings
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

SITE_ID = 1

try:
    from .production_settings import *
except ImportError:
    pass
