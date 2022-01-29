"""
Django settings for moinproject project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY','django-insecure-4t%9-m-rpfaud^os53_0e9u-s)w)4hb)+(zfq1n*=jkhuhskq7')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG', 'True') != 'False')

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'account.User'
AUTH_FOLLOWER_MODEL = "account.User"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'moinapp',
    'account',
    'moin_1',
    'moin_2',
    'moin_3',
    'moin_4',
    'moin_5',
    'moin_6',
    'moin_7',
    'moin_8',
    'moin_9',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'moinproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['moinproject/templates'],
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

WSGI_APPLICATION = 'moinproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFIELS_DIRS = [
    os.path.join(BASE_DIR, 'moinapp', 'static'),
    os.path.join(BASE_DIR, 'account', 'static'),
    os.path.join(BASE_DIR, 'moin_1', 'static'),
    os.path.join(BASE_DIR, 'moin_2', 'static'),
    os.path.join(BASE_DIR, 'moin_3', 'static'),
    os.path.join(BASE_DIR, 'moin_4', 'static'),
    os.path.join(BASE_DIR, 'moin_5', 'static'),
    os.path.join(BASE_DIR, 'moin_6', 'static'),
    os.path.join(BASE_DIR, 'moin_7', 'static'),
    os.path.join(BASE_DIR, 'moin_8', 'static'),
    os.path.join(BASE_DIR, 'moin_9', 'static'),
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'moin-static'
AWS_S3_CUSTOM_DOMAIN = f's3.{AWS_REGION}.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}'

AWS_S3_FILE_OVERWRITE = False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl':'max-age=86400',
}

AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = ''
STATIC_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILES_STORAGE = 'moinproject.s3media.MediaStorage'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)