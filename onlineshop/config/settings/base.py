"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# ===== 경로 설정 ======
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = os.path.dirname(BASE_DIR)
# ==========================

# ===== SECRET FILE 경로 설정 =====
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, ".config_secret")
CONFIG_SECRET_FILE = os.path.join(CONFIG_SECRET_DIR, "settings_develop.json")
# =================================

# ======= SECRET FILE json으로 가져오기 ========
import json

if os.path.isfile(CONFIG_SECRET_FILE):
    # 로컬 환경 또는 배포 환경
    config_secret_file = json.loads(open(CONFIG_SECRET_FILE).read())
else:
    # 테스팅 환경 (환경변수로 지정해야댐)
    config_secret_file = json.loads(os.environ["SECRET_SETTING"])
# ======================================

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # 사이트 정보 설정
    "storages",
    "allauth",
    "allauth.account",  # 가입한 게정 관리
    "allauth.socialaccount",  # 소셜계정으로 가입한 게정 관리
    "allauth.socialaccount.providers.naver",  # 네이버를 사용한 소셜로그인
    "shop",
    "cart",
    "coupon",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(ROOT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Authentication setting
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID = 1
LOGIN_REDIRECT_URL = "/"


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


AWS_ACCESS_KEY_ID = config_secret_file["aws"]["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = config_secret_file["aws"]["AWS_SECRET_ACCESS_KEY"]
AWS_REGION = config_secret_file["aws"]["AWS_REGION"]
AWS_STORAGE_BUCKET_NAME = config_secret_file["aws"]["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_CUSTOM_DOMAIN = config_secret_file["aws"]["AWS_S3_CUSTOM_DOMAIN"]
AWS_S3_OBJECT_PARAMETERS = config_secret_file["aws"]["AWS_S3_OBJECT_PARAMETERS"]
# AWS_DEFAULT_ACL = None
AWS_DEFAULT_ACL = config_secret_file["aws"]["AWS_DEFAULT_ACL"]
AWS_LOCATION = config_secret_file["aws"]["AWS_LOCATION"]

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

DEFAULT_FILE_STORAGE = "config.asset_storage.MediaStorage"

# CART SESSION SETTING
CART_ID = "cart_in_session"
