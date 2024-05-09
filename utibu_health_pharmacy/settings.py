from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# Adjust allowed hosts based on debug mode
ALLOWED_HOSTS = []

if not DEBUG:
    ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'pharmacy.apps.PharmacyConfig',
    'rest_framework',
    'drf_spectacular',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'utibu_health_pharmacy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'utibu_health_pharmacy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Use SQLite database by default
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Override database settings in production mode
if not DEBUG:
    # DATABASES['default'] = dj_database_url.parse(config('EXTERNAL_DB_URL'))
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Define the URL and root directory for static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Define the URL and root directory for media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Define the login URL
LOGIN_URL = 'pharmacy/login/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# DRF Spectacular settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Utibu Health Pharmacy API',
    'DESCRIPTION': 'API for interacting with Utibu Health Pharmacy database to serve customers through a mobile app.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

MPESA_API = {
    "BIZ_SHORT_CODE": config('BIZ_SHORT_CODE'),
    "CALLBACK_URL": config('CALLBACK_URL'),
    "PAYMENT_URL": config('PAYMENT_URL'),
    "CREDENTIALS_URL": config('CREDENTIALS_URL'),
    "CONSUMER_KEY": config('CONSUMER_KEY'),
    "CONSUMER_SECRET": config('CONSUMER_SECRET'),
    "PASS_KEY": config('PASS_KEY'),
}

# MPESA_API = {
#     "BIZ_SHORT_CODE": '174379',
#     "CALLBACK_URL": 'https://a93c-102-140-253-159.ngrok-free.app/pharmacy/mpesa-callback',
#     "PAYMENT_URL": 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',
#     "CREDENTIALS_URL": 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
#     "CONSUMER_KEY": 'yEMHYsHPGjo8W6GHvAAYAq6GfVE7wuFdpabdrwJ7USkJTxMN',
#     "CONSUMER_SECRET": 'KchCdWviooa4X5xYa1d9KBc8wFXuLac9nysqVLKpG4zgUMdeEuRxdHMsKPdvVKG6',
#     "PASS_KEY": 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919',
# }
