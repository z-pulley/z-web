import logging
import os.path

DIRNAME = os.path.dirname(os.path.abspath(__file__))
DEBUG=True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
          ('Aaron Racicot','aaronr@z-pulley.com'),
)

MANAGERS = ADMINS

## Root URL structure
ROOT_RELATIVE_URL = '/'
ROOT_URL = 'http://www.z-pulley.com' + ROOT_RELATIVE_URL
LOGIN_URL = ROOT_URL + 'accounts/login/'

#DOC_ROOT = os.path.join(DIRNAME, 'z-pulley_sphinx/build/html')

STATS_ROOT = os.path.join(DIRNAME, 'webalizer/stats')

## For registration
ACCOUNT_ACTIVATION_DAYS = 7

# For profiles
AUTH_PROFILE_MODULE = 'profiles.userprofile'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'z_web',
        'USER': 'aaronr',
        'PASSWORD': 'aaronr',
        'HOST': '',
        'PORT': '',
    },
}       

FIXTURE_DIRS = (
    os.path.join(DIRNAME, 'z_web/fixtures'),
    )


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = ''
MEDIA_ROOT = os.path.join(DIRNAME, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ROOT_URL + 'media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_ROOT = os.path.join(DIRNAME, 'admin-media')
ADMIN_MEDIA_PREFIX = ROOT_URL + 'admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lkjsfalkj;lakjeweqlkjv98cx7v98saufdjsfadsflkajkdsljfkdsa^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS=(
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    'context.context_processors.root_relative_url',
)

#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.RemoteUserBackend',
#)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    #'django.contrib.gis',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'z_web',
)

try:
    from local_settings import *
except ImportError, exp:
    pass
