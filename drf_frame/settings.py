#coding:utf-8


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import  path
from datetime import timedelta

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fs7=-(4d^smyu!ielpa=lm8@3+jvo8$k0izhr-ltvbaj%!q)-c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'framework',
    'rest_framework.authtoken',
    'djcelery',
    'webui',
    'pagination_bootstrap',
)
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

ROOT_URLCONF = 'drf_frame.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                'django.core.context_processors.request',
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'drf_frame.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {

    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'drf_frame',
    'USER': 'root',
    'PASSWORD': 'hugo9091',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'MAX_CONN_AGE': '3600'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = path.join(PROJECT_ROOT, 'static').replace('\\', '/')
MEDIA_ROOT = path.join(PROJECT_ROOT, 'media').replace('\\', '/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

#REST_FRAMEWORK全局设置
REST_FRAMEWORK ={
    #分页
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':5,
    #权限
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    #认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
   ),
}

#日志配置
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'formatters': {
    'standard': {
        'format': '[%(asctime)s] %(levelname)s %(module)s.%(funcName)s-[%(lineno)d] %(message)s'}  #日志格式
},
'filters': {
    'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
    }
},
'handlers': {
    'default': {
        'level':'INFO',
        'class':'logging.handlers.RotatingFileHandler',
        'filename': 'logs/drf_frame.log',
        'maxBytes': 1024*1024*5,                  #文件大小
        'backupCount': 1,                         #备份份数
        'formatter':'standard',                   #使用哪种formatters日志格式
    },
    'info': {
        'level': 'INFO',
        'class': 'logging.FileHandler',
        'filename': 'logs/drf_frame-info.log',
        'formatter':'standard',
    },
    'error': {
        'level': 'ERROR',
        'class': 'logging.FileHandler',
        'filename': 'logs/drf_frame-error.log',
        'formatter':'standard',
    },

},
'loggers': {
    'log_info': {
        'handlers': ['info'],
        'level': 'INFO',
        'propagate': True
    },
    'log_error': {
        'handlers': ['error'],
        'level': 'ERROR',
        'propagate': True
    }

  }
}


#celery
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
# BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'amqp://'
BROKER_URL = 'amqp://hugo:hugo9091@localhost:5672/loghost'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
