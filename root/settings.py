from datetime import timedelta
from os.path import join
from pathlib import Path

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-$$^lzx*%#*0fz9xx^9a#d#04@eh9y-qr$p&%-g+b9fe=rrajdo'

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [

    'unfold',  # Admin panel config

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My app
    'user',

    # Third party app
    'rest_framework_simplejwt',  # JWT config
    'drf_spectacular',  # Swagger config

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

ROOT_URLCONF = 'root.urls'

WSGI_APPLICATION = 'root.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


STATIC_URL = 'static/'
STATIC_ROOT = join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],       # templates papkasi yo‘q bo‘lsa ham bo‘sh qoldirsa bo‘ladi
        'APP_DIRS': True,                       # bu True bo‘lishi kerak, chunki admin o‘z templateslarini topadi
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



# =-=-=-=-=-=-=-=-=-=-=-=-=-= DRF CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',),

    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}


# =-=-=-=-=-=-=-=-=-=-=-=-=-= JWT CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=


SPECTACULAR_SETTINGS = {
    'TITLE': 'Parkovka BW Project API',
    'DESCRIPTION': 'Mit shtarkem has gegden shtrom ',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,  # Media file uchun
}

# =-=-=-=-=-=-=-=-=-=-=-=-=-= Auth CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=

# AUTH_USER_MODEL = 'user.User'
AUTH_USER_MODEL = 'user.User'

# =-=-=-=-=-=-=-=-=-=-=-=-=-= Celery CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Tashkent'

# =-=-=-=-=-=-=-=-=-=-=-=-=-= Gmail CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server host
EMAIL_PORT = 587  # SMTP server port (587 for TLS, 465 for SSL)
EMAIL_USE_TLS = True  # True for TLS, False for SSL
EMAIL_HOST_USER = 'artyom.bw08@gmail.com'  # SMTP server username
EMAIL_HOST_PASSWORD = 'ecwuhvzdscaqkjxt'  # SMTP server password
EMAIL_USE_SSL = False  # Set to True if using SSL
DEFAULT_FROM_EMAIL = 'artyom.bw08@gmail.com'  # Default sender email address


# =-=-=-=-=-=-=-=-=-=-=-=-=-= JWT CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=3),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(hours=4),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

# =-=-=-=-=-=-=-=-=-=-=-=-=-= Unfold CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=

UNFOLD = {
    "SHOW_VIEW_ON_SITE": False,
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Files"),
                "separator": False,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Uploaded Files"),
                        "icon": "upload_file",
                        "link": reverse_lazy("admin:user_uploadedfile_changelist"),
                    },
                ],
            },
        ],
    }
}

# =-=-=-=-=-=-=-=-=-=-=-=-=-= Loging CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}
