"""
Django settings for ModelProject project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$&#y_(!e4(m#k6o32=^u6(qm@g0qf1s9($w2m*-sdz5zx!b0(l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #установлено в рамках проекта
    'NewsPortal',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fpages',
    'django_filters',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

DEFAULT_FROM_EMAIL = 'Leemur1504@yandex.ru'

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # установлено в рамках проекта
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'ModelProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'ModelProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/posts/'
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'Leemur1504@yandex.ru'
EMAIL_HOST_PASSWORD = 'Narukami88'
EMAIL_USE_SSL = True

CELERY_BROKER_URL = 'redis://default:Z8uSNPYwpxZXEJQplVxZNvNBJY8NOaVJ@redis-18688.c14.us-east-1-3.ec2.cloud.redislabs.com:18688'
CELERY_RESULT_BACKEND = 'redis://default:Z8uSNPYwpxZXEJQplVxZNvNBJY8NOaVJ@redis-18688.c14.us-east-1-3.ec2.cloud.redislabs.com:18688'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, '../cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style' : '{',
    'formatters': {
        'simple': {'format': '{asctime} {levelname} {message}'},
        'verbose_1': {'format': '{asctime} {levelname} {message} {pathname}'},
        'verbose_2': {'format': '{asctime} {levelname} {message} {pathname} {exc_info}'},
    },
    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}
    },
    'handlers': {
        'console': {
            {'level': 'DEBUG','filters': ['require_debug_true'],'class': 'logging.StreamHandler','formatter': 'simple'},
            {'level': 'WARNING', 'filters': ['require_debug_true'],'class': 'logging.StreamHandler','formatter': 'verbose_1'},
            {'level': 'ERROR', 'filters': ['require_debug_true'],'class': 'logging.StreamHandler','formatter': 'verbose_2'},
        },
        'mail_admins': {'level': 'ERROR', 'filters': ['require_debug_false'],'class': 'django.utils.log.AdminEmailHandler', 'formatter': 'verbose_1'}
    },
    'loggers': {
        'django': {'handlers': ['console'],'propagate': True},
        'django.request': {'handlers': ['mail_admins'],'level': 'ERROR','propagate': True},
        'django_server': {'handlers': ['mail_admins'],'level': 'ERROR','propagate': True}
    }
}