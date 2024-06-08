from pathlib import Path

import environ
from django.contrib import admin

from config.custom_admin import myadmin

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(Path.joinpath(BASE_DIR, ".env"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.str("ALLOWED_HOSTS", []).split(",")
CSRF_TRUSTED_ORIGINS = env.str("CSRF_TRUSTED_ORIGINS", ["http://localhost"]).split(",")

CUSTOM_APPS = [
    "core",
    "website",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "solo.apps.SoloAppConfig",
    *CUSTOM_APPS,
]

if DEBUG:
    INSTALLED_APPS += [
        "drf_spectacular",
        "django_extensions",
    ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "data/db.sqlite3",
    }
}

REDIS_HOST = env.str("REDIS_HOST")
REDIS_PORT = env.int("REDIS_PORT")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}",
    }
}
CACHE_MIDDLEWARE_SECONDS = 3000

AUTH_USER_MODEL = "core.User"

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Asia/Krasnoyarsk"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = Path.joinpath(BASE_DIR, "static")
STATICFILES_DIR = [
    Path.joinpath(BASE_DIR, "static"),
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ADMIN_SITE = "core.custom_admin.MyAdminSite"

admin.site = myadmin
admin.sites.site = myadmin

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}

PHONENUMBER_DEFAULT_REGION = "RU"

BOT_TOKEN = env.str("BOT_TOKEN")

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = "smtp.gmail.com"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST_USER = env.str("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = env.str("EMAIL_PASS")
EMAIL_PORT = 587
