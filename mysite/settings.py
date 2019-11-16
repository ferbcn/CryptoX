"""
Django settings for pizza project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
#import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
print("Settings is retrieving Django Secret KEY...")
print("Django is running on PID: ", os.getpid())
SECRET_KEY = None

try:
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
    print ("Secret Key found in environment!")
except KeyError:
    print ("Secret Key Not found in environment!")
    try:
        from config import DJANGO_SECRET_KEY
        SECRET_KEY = DJANGO_SECRET_KEY
        print ("Secret Key found in config file!")
    except Exception:
        print ("Secret Key Not found in config file!")
        print ("No secret Key found! Bye.")
        sys.exit()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'f-cryptox.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'cryptoweb.apps.CryptoWebConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# local DB: sqlit3
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

# PostgreSQL DB on Heroku (read environmental variables)
try:
    # Heroku PostgreSQL Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ["Database"],
            'USER': os.environ["User"],
            'PASSWORD': os.environ["Password"],
            'HOST': os.environ["Host"],
            'PORT': os.environ["Port"],
        }
    }
    print ("DB config found in environment!")
    #print(DATABASES)
except KeyError:
    print ("DB config Not found in environment!")
    try:
        from config import DATABASES
        print ("DB config found in config file!")
    except Exception:
        print ("DB config Not found in config file!")
        print ("No DB config found! Bye.")
        #sys.exit()


# Heroku PostgreSQL DB
#   Database Config or URL loaded from environment or config.py


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'cryptoweb/static'),)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
