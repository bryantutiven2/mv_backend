"""
Django settings for ServidorMapaVirtual project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
# 10/11/2020
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
from django.conf.global_settings import DATA_UPLOAD_MAX_MEMORY_SIZE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dl_xihb33_il*jo!=b+ia2%+9&wtaxu(mz=x1%u9ar$sa@!w#g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# para token de password 10/11/2020
PASSWORD_RESET_TIMEOUT_DAYS = 1

ALLOWED_HOSTS = []

#Cors
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = [
   'Access-Control-Allow-Origin',
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ORIGIN_WHITELIST = [
  'http://localhost:4200',
  'http://localhost:8000',
  'http://localhost:8100',
    'http://192.168.0.112:8100',
]
ALLOWED_HOSTS = ['192.168.0.112', 'localhost', '127.0.0.1']
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'serviciosBackend',
    # 'oauth2_provider',
    # 'social_django',
    # 'rest_framework_social_oauth2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'ServidorMapaVirtual.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ServidorMapaVirtual.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MapaVirtual',
        'USER': 'root',
        'PASSWORD' : 'toby',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

AUTH_USER_MODEL= 'serviciosBackend.User'
# DRFSO2_PROPRIETARY_BACKEND_NAME = 'ServidorMapaVirtual'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        # 'rest_framework_social_oauth2.authentication.SocialAuthentication',
    )
}

AUTHENTICATION_BACKENDS = (
   # Facebook OAuth2
   #  'social_core.backends.facebook.FacebookAppOAuth2',
   #  'social_core.backends.facebook.FacebookOAuth2',

    # django-rest-framework-social-oauth2
    # 'rest_framework_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)

# Facebook configuration
# SOCIAL_AUTH_FACEBOOK_KEY = '921830748297038'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'fc9a9177662cd1eb9985d3aa6e856fe4'
# SOCIAL_AUTH_FACEBOOK_KEY = '603186720557884'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'b4c4bd5fd8d9c832961466389749ac8e'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#     'fields': 'id, name, email, first_name'
# }

#configuraciones por default para el token
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    #cambiar el prefix para autenticacion
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=180),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# configuación para enviar email desde gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("PASSWORDEMAIL")
