from os import getenv
from pathlib import Path

BOOLEAN_MAP = {
    "True": True,
    "False": False
}

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv("SECRET_KEY", "dummy-secret-key")

DEBUG = BOOLEAN_MAP.get(getenv("DEBUG"), False)

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "storages",

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
]

ROOT_URLCONF = 'boilerplate.urls'

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

WSGI_APPLICATION = 'boilerplate.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        "HOST": getenv("DB_HOST", "db"),
        "PORT": getenv("DB_PORT", 5432),
        "NAME": getenv("DB_NAME", "postgres"),
        "USER": getenv("DB_USER", "postgres"),
        "PASSWORD": getenv("DB_PASS", "postgres")
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# AWS
AWS_SECRET_ACCESS_KEY = getenv("S3_SECRET_KEY")
AWS_ACCESS_KEY_ID = getenv("S3_ACCESS_KEY")

AWS_S3_HOST = getenv("AWS_URL", "minio")
# AWS_S3_ENDPOINT_URL = getenv("AWS_URL", "minio")

AWS_STORAGE_BUCKET_NAME = getenv("AWS_BUCKET_NAME", "boilerplate")
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = "public-read"

# Static files (CSS, JavaScript, Images)
STATIC_URL = getenv("STATIC_URL", "/static/")
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_STORAGE = "boilerplate.storages.StaticStorage"

# Media
MEDIA_URL = getenv("MEDIA_URL", "/media/")
MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_FILE_STORAGE = "boilerplate.storages.MediaStorage"

LOCALE = ((BASE_DIR / "locale/"),)
