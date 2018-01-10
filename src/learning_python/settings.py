import os
import datetime
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^(&2eky(w(=r5y%^zvn5b2r)=jf@hs-r2)53aduauc*ynrw#44'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["54.68.96.141", "localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'crispy_forms',
    'haystack',
    'markdownx',
    'pagedown',
    'rest_framework',
    'rest_framework_swagger',
    'social_django',
    'corsheaders',

    # app
    'accounts',
    'comments',
    'posts',
    'tags',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',   
]

CORS_ORIGIN_ALLOW_ALL = True   

ROOT_URLCONF = 'learning_python.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'learning_python.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'learning_python',
        'USER': 'root',
        'PASSWORD': 'Miamikki521',
        'HOST': 'localhost',
        'PORT': '3306',
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

LOGIN_URL = "/accounts/login/"

LANGUAGES = (
    ('en', _('English')),
    ('ja', _('Japanese')),
    ('vi', _('Vietnamese')),
)
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'),]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

AUTH_USER_MODEL = 'accounts.MyUser'

SECRET_KEY = "test123"

SECURITY_PASSWORD_SALT = "test321"

# gmail settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'test29051993@gmail.com'
EMAIL_HOST_PASSWORD = 'Minh1234'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    'EXCEPTION_HANDLER': 'learning_python.utils.customer_exception_handler',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 1
}


MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.sane_lists',
    'markdown.extensions.nl2br',
    'markdown.extensions.extra',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)


LOGIN_REDIRECT_URL = 'home'

SOCIAL_AUTH_GITHUB_KEY = '49aa0f62b6e4331d0681'
SOCIAL_AUTH_GITHUB_SECRET = '9945f15b35e729909038948ea542d0f2ae81c492'

SOCIAL_AUTH_TWITTER_KEY = 'dX9VC75etjgCYdgZPxXypCHdN'
SOCIAL_AUTH_TWITTER_SECRET = 'S6KQKUhC3g3tcsbrpFxDYVevxCF2AfhPy5ZHwBhMGmOPL2bue8'

SOCIAL_AUTH_FACEBOOK_KEY = '1582699971777486'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'f1a4cc90f08196068e24f6104d58225e'  # App Secret


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
    
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:9000'
)