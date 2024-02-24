from pathlib import Path
from datetime import timedelta
import environ


env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR/'.env')


SECRET_KEY = 'django-insecure-$+eyrm&&gge&$jn^jh%n^eess%xuhj$ifqym+i1nxu_#jtxdh='  # NOQA

DEBUG = True

HOSTS = [
    'ursasplanet.com',
    'api.ursasplanet.com',
    'localhost',
    'leks.hooli.xyz'
]

ORIGINS = [
    'https://ursasplanet.com',
    'https://sprint.ursasplanet.com',
    'https://api.ursasplanet.com',
    'http://localhost:3000',
    'http://leks.hooli.xyz:3000'
]

ALLOWED_HOSTS = HOSTS

CSRF_TRUSTED_ORIGINS = ORIGINS
CORS_ALLOWED_ORIGINS = ORIGINS
CORS_ORIGIN_WHITELIST = ORIGINS

CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_celery_results',
    'django_celery_beat',
    'rest_framework',
    'rest_framework_simplejwt',
    "corsheaders",
    'image_optimizer',

    'apps.users',
    'apps.projects',
    'apps.wallets',
    'apps.web3auth',
    'apps.socials',

    'apps.tasks',
    'apps.tasks.socials.discord',
    'apps.tasks.socials.twitter',
    'apps.tasks.socials.telegram',
    'apps.tasks.socials.github',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # NOQA
    },
]


LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR/'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'users.User'


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # NOQA
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'apps.web3auth.authenticate.CustomAuthentication',
    )
}

CELERY_TIMEZONE = "Australia/Tasmania"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'


SIMPLE_JWT = {
    'AUTH_COOKIE': 'access_token',
    'AUTH_COOKIE_SECURE': False,
    'AUTH_COOKIE_HTTP_ONLY': True,
    'AUTH_COOKIE_PATH': '/',
    'AUTH_COOKIE_SAMESITE': 'Lax',
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3)
}

REFERRER_COOKIE = {
    'COOKIE': 'referrer',
    'SECURE': False,
    'HTTP_ONLY': True,
    'PATH': '/',
    'SAMESITE': 'Lax',
    'LIFETIME': timedelta(days=3)
}

OPTIMIZED_IMAGE_METHOD = 'pillow'

DEFAULT_FROM_EMAIL = env('EMAIL_HOST_USER')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True


SOCIAL_REDIRECT_URI_PREFIX = env('SOCIAL_REDIRECT_URI_PREFIX')

GITHUB_CLIENT_ID = env('GITHUB_CLIENT_ID')
GITHUB_SECRET_KEY = env('GITHUB_SECRET_KEY')
GITHUB_REDIRECT_URI = env('SOCIAL_REDIRECT_URI_PREFIX')+'github'

DISCORD_CLIENT_ID = env('DISCORD_CLIENT_ID')
DISCORD_SECRET_KEY = env('DISCORD_SECRET_KEY')
DISCORD_REDIRECT_URI = env('SOCIAL_REDIRECT_URI_PREFIX')+'discord'

X_CLIENT_ID = env('X_CLIENT_ID')
X_CLIENT_SECRET = env('X_CLIENT_SECRET')
X_REDIRECT_URI = env('SOCIAL_REDIRECT_URI_PREFIX')+'x'

TELEGRAM_BOT_TOKEN = env('TELEGRAM_BOT_TOKEN')
