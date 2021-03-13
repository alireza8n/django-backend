from os import getenv
from pathlib import Path

BOOLEAN_MAP = {
    "True": True,
    "False": False
}

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv("SECRET_KEY", "dummy-secret-key")

DEBUG = BOOLEAN_MAP.get(getenv("DEBUG"), False)

HOST = getenv('HOST', 'localhost')

ALLOWED_HOSTS = [HOST]

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

AWS_S3_ENDPOINT_URL = getenv("AWS_URL", "http://minio:9000")

AWS_STORAGE_BUCKET_NAME = getenv("AWS_BUCKET_NAME", "boilerplate")
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = "public-read"
AWS_S3_CUSTOM_DOMAIN = '{}:9000/{}'.format(HOST, AWS_STORAGE_BUCKET_NAME)
AWS_S3_USE_SSL = not DEBUG
AWS_S3_SECURE_URLS = not DEBUG

# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = "boilerplate.storages.StaticStorage"

# Media
DEFAULT_FILE_STORAGE = "boilerplate.storages.MediaStorage"

LOCALE = ((BASE_DIR / "locale/"),)


from botocore.client import ClientError
from storages.backends.s3boto3 import S3Boto3Storage

s3 = S3Boto3Storage()
try:
    s3.connection.meta.client.head_bucket(Bucket=AWS_STORAGE_BUCKET_NAME)
except ClientError:
    s3.connection.meta.client.create_bucket(Bucket=AWS_STORAGE_BUCKET_NAME)
