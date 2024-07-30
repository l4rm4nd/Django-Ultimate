"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import pytz
import secrets
from django.utils.html import escape

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# get debug modus from env
DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true']

# get container version from env
VERSION = escape(os.environ.get("VERSION", ''))

# auto-generate a secure secret key or use from env variable
SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_urlsafe(32))

# define allowed hosts and trusted domains via env variables
DOMAIN = ""
ALLOWED_HOSTS = ["127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000"]

DOMAIN = str(os.environ.get("DOMAIN", "localhost"))
TRUSTED_PORT = str(os.environ.get("PORT", "8000"))
SECURE_COOKIES = str(os.environ.get("SECURE_COOKIES", "False"))

if DOMAIN:
    DOMAIN = DOMAIN.rstrip('/').replace('http://', '').replace('https://', '')
    ALLOWED_HOSTS.append(DOMAIN)
    TRUSTED_USER_DOMAIN_HTTP = f"http://{DOMAIN}:{TRUSTED_PORT}"
    TRUSTED_USER_DOMAIN_HTTP_80_DEFAULT = f"http://{DOMAIN}"
    TRUSTED_USER_DOMAIN_HTTPS = f"https://{DOMAIN}:{TRUSTED_PORT}"
    TRUSTED_USER_DOMAIN_HTTPS_443_DEFAULT = f"https://{DOMAIN}"
    CSRF_TRUSTED_ORIGINS.extend([TRUSTED_USER_DOMAIN_HTTP, TRUSTED_USER_DOMAIN_HTTPS, TRUSTED_USER_DOMAIN_HTTP_80_DEFAULT, TRUSTED_USER_DOMAIN_HTTPS_443_DEFAULT])

#Session Management
CSRF_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 30*60 # 30 minute session age
SESSION_COOKIE_NAME = 'Session'
SESSION_COOKIE_SAMESITE = 'Lax'

if SECURE_COOKIES == "False":
    # transmit cookies over unencrypted http
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    # transmit cookies over encrypted https only
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # also set hsts response header
    SECURE_HSTS_SECONDS = "31536000"
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# http security response headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
REFERRER_POLICY = 'same-origin'
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://fonts.googleapis.com")
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'")
CSP_FONT_SRC = ("'self'", "https://fonts.googleapis.com", "https://fonts.gstatic.com")
CSP_IMG_SRC = ("'self'", 'data:')
CSP_OBJECT_SRC = ("'none'",)
CSP_CONNECT_SRC = ("'self'",)

# Application definition
INSTALLED_APPS = [
    'myapp',
    'django_celery_beat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates/registration')],
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

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database', 'db.sqlite3'),
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
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Celery configuration
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

if os.environ.get('REDIS_HOST') == None:
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
else:
    redis_host = os.environ.get('REDIS_HOST')
    CELERY_BROKER_URL = f'redis://{redis_host}:6379/0'
    CELERY_RESULT_BACKEND = f'redis://{redis_host}:6379/0'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Berlin'
DJANGO_CELERY_BEAT_TZ_AWARE = True
CELERY_ENABLE_UTC = False
CELERY_WORKER_LOG_FILE = os.path.join(LOGS_DIR, 'celery_worker.log')
CELERY_BEAT_LOG_FILE = os.path.join(LOGS_DIR, 'celery_beat.log')

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

WSGI_APPLICATION = 'myproject.wsgi.application'

# check if oidc is enabled
OIDC_ENABLED = os.environ.get('OIDC_ENABLED', 'False').lower() in ['true']

if OIDC_ENABLED:
    # get oidc config from env
    OIDC_CREATE_USER = os.environ.get('OIDC_CREATE_USER', 'True').lower() in ['true']
    OIDC_RP_SIGN_ALGO = os.environ.get('OIDC_RP_SIGN_ALGO', 'HS256')
    OIDC_OP_JWKS_ENDPOINT = os.environ.get('OIDC_OP_JWKS_ENDPOINT')
    OIDC_RP_IDP_SIGN_KEY = os.environ.get('OIDC_RP_IDP_SIGN_KEY')
    OIDC_RP_CLIENT_ID = os.environ.get('OIDC_RP_CLIENT_ID')
    OIDC_RP_CLIENT_SECRET = os.environ.get('OIDC_RP_CLIENT_SECRET')
    OIDC_OP_AUTHORIZATION_ENDPOINT = os.environ.get('OIDC_OP_AUTHORIZATION_ENDPOINT')
    OIDC_OP_TOKEN_ENDPOINT = os.environ.get('OIDC_OP_TOKEN_ENDPOINT')
    OIDC_OP_USER_ENDPOINT = os.environ.get('OIDC_OP_USER_ENDPOINT')
    OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS = os.environ.get('OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS', 900)
    OIDC_USERNAME_ALGO = 'myapp.utils.generate_username'

    # Add 'mozilla_django_oidc.middleware.SessionRefresh' to INSTALLED_APPS
    INSTALLED_APPS.append('mozilla_django_oidc')
    
    # Add 'mozilla_django_oidc' authentication backend
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    )

    # Add 'mozilla_django_oidc.middleware.SessionRefresh' to MIDDLEWARE
    MIDDLEWARE.append('mozilla_django_oidc.middleware.SessionRefresh')

    # Fix http callback issue in mozilla-django-oidc by forcing https; https://github.com/mozilla/mozilla-django-oidc/issues/417
    # OIDC should only be setup behind a TLS reverse proxy anyways
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
