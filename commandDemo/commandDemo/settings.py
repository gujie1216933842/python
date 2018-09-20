"""
Django settings for commandDemo project.

Generated by 'django-admin startproject' using Django 1.11.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5pqvqcty7zu20*w8a)+v8cm+c!j69^ne*%$6fyqjlt)+z85yvw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',
    'sencondapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'commandDemo.urls'

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

WSGI_APPLICATION = 'commandDemo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'scratch_card',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': '47.97.165.75',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
CURRENT_DATE_STR = 1
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s:%(lineno)s %(message)s',
        },
        'simple': {
            'format': '%(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'backupCount': 365,
            'filename': os.path.join(BASE_DIR, 'logs', 'debug_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'backupCount': 365,
            'filename': os.path.join(BASE_DIR, 'logs', 'errors_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'ant_main': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_main_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'ant_intf': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'backupCount': 365,
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_intf_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'kb_main': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'backupCount': 365,
            'filename': os.path.join(BASE_DIR, 'logs', 'kb_main_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'kb_intf': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'backupCount': 365,
            'filename': os.path.join(BASE_DIR, 'logs', 'kb_intf_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'smtp_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.SMTPHandler',
            'formatter': 'verbose',
            'mailhost': 'smtpdm.aliyun.com',
            'fromaddr': 'typhon-no-reply@smtp2.rrd.com.cn',
            'toaddrs': ['admin@admin.com', ],
            'subject': 'typhon api error log',
            'credentials': ('typhon-no-reply@smtp2.rrd.com.cn', 'HellO13579'),
        },
        'ant_produce_query': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_produce_query_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'ant_produce_complete': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_produce_complete_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'ant_delivery_query': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_delivery_query_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'ant_delivery_complete': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_delivery_complete_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'ant_produce_package': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_produce_package_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'ant_delivery_package': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_delivery_package_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        },
        'ant_transfer_package': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': os.path.join(BASE_DIR, 'logs', 'ant_transfer_package_{}.log'.format(CURRENT_DATE_STR)),
            'formatter': 'verbose'
        }
    },
    'loggers': {
        # Django loggers
        'django': {
            # 'handlers': ['null'],
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        # POD core loggers
        # Add by TX
        'ant_main': {
            'handlers': ['ant_main', 'debug_file', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_intf': {
            'handlers': ['debug_file', 'ant_intf', 'error_file', 'console', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_importto_task': {
            'handlers': ['debug_file', 'ant_intf', 'error_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'kb_main': {
            'handlers': ['kb_main', 'debug_file', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'kb_intf': {
            'handlers': ['debug_file', 'kb_intf', 'error_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django_crontab.crontab': {
            'handlers': ['debug_file', 'ant_intf', 'error_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_produce_query': {
            'handlers': ['ant_produce_query', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_produce_complete': {
            'handlers': ['ant_produce_complete', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_delivery_query': {
            'handlers': ['ant_delivery_query', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_delivery_complete': {
            'handlers': ['ant_delivery_complete', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_produce_package': {
            'handlers': ['ant_produce_package', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_delivery_package': {
            'handlers': ['ant_delivery_package', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ant_transfer_package': {
            'handlers': ['ant_transfer_package', 'console', 'error_file', 'smtp_handler'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}
