"""
Django settings for config project.

Generated by 'django-admin startproject' using Django.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import socket  # required for django-debug-toolbar with Docker, see below
from pathlib import Path
from environs import Env  # environs[django]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# environs[django]
env = Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Uses environs[django]
SECRET_KEY = env.str("SECRET_KEY")  # Raises django's ImproperlyConfigured exception \
# if SECRET_KEY not in .env

# SECURITY WARNING: don't run with debug turned on in production!
# Uses environs[django]
DEBUG = env.bool("DEBUG", default=False)  # False if not in .env

# Uses environs[django]
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Applications definition
# Split apps into DJANGO_CORE_APPS, THIRD_PARTY_APPS & PROJECT_APPS
# Then combine into INSTALLED_APPS

DJANGO_CORE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    # django-allauth apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.bitbucket_oauth2",
    # miscellaneous apps
    "crispy_forms",
    "debug_toolbar",
    "django_extensions",
    "import_export",
]

LOCAL_PROJECT_APPS = [
    "apps.pages.apps.PagesConfig",  # aka pages in djangox, cookiecutter etc
    "apps.common.apps.CommonConfig",
    "apps.accounts.apps.AccountsConfig",
    "apps.agencies.apps.AgenciesConfig",
    "apps.astronauts.apps.AstronautsConfig",
    "apps.evas.apps.EvasConfig",
    "apps.missions.apps.MissionsConfig",
]

INSTALLED_APPS = DJANGO_CORE_APPS + THIRD_PARTY_APPS + LOCAL_PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# Set rootconf to project.urls
# https://docs.djangoproject.com/en/3.1/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # DIRS edited to best practise - one project-level 'templates' directory
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
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

# https://docs.djangoproject.com/en/4.0/ref/settings/#wsgi-applicatio
WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# Uses environs[django]
DATABASES = {"default": env.dj_db_url("DATABASE_URL")}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "static/"
# 'STATICFILES_DIRS' defines the location of static files in local development
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]

# 'STATIC_ROOT' defines the location of static files for production
# During deployment use collectstatic command to gather all static files into single directory
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))

# 'STATICFILES_FINDERS' defines how Django looks for static file directories
# These settings are implicit during setup but defining explicitly here for understanding
STATICFILES_FINDERS = [
    # Look within STATICFILES_DIRS set above to project-level 'static' directory
    "django.contrib.staticfiles.finders.FileSystemFinder",
    # Look for any individual app-level 'static' directories
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Media files (User uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR.joinpath("media"))

# Bootstrap Crispy-Forms settings
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Settings for django-debug-toolbar
# Normal local setting
# INTERNAL_IPS = ['127.0.0.1']
# Since web server is running within Docker an additional step is required so
#   that it matches the machine address of Docker
if DEBUG:
    import os  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

# Authentication settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # allauth specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

AUTH_USER_MODEL = "accounts.CustomUser"

# DJANGO-ALLAUTH SETTINGS
# Site id required for using 'sites' framework with django-allauth
SITE_ID = 1

LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

# Don't authenticate by usernames, use emails instead, but still request a username(nickname)
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"  # nickname in allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False

# Allow login via email or username
ACCOUNT_AUTHENTICATION_METHOD = "email"

# Default is 'True', use 'optional' for development purposes
ACCOUNT_EMAIL_VERIFICATION = "optional"

# Default is 'True'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# Controls life time of the session, default is 'None' to ask user "Remember me?"
ACCOUNT_SESSION_REMEMBER = None

# controls whether or not the endpoints for initiating a social login (for example, "/accounts/google/login/") require a POST request to initiate the handshake. As requiring a POST is more secure, the default of this new setting is `False`
SOCIALACCOUNT_LOGIN_ON_GET = False

# DJANGO-IMPORT-EXPORT SETTINGS
IMPORT_EXPORT_USE_TRANSACTIONS = True

# DJANGO-EXTENSIONS SETTINGS
SHELL_PLUS_IMPORTS = [
    "from pprint import pprint",
]
