from pathlib import Path
import environ
from datetime import timedelta
import os

# Создаем экземпляр Environ
env = environ.Env(
    DEBUG=(bool, False)
)

# Определяем базовую директорию проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Проверяем, какое окружение используется (разработка/продакшн)
ENVIRONMENT = env('DJANGO_ENVIRONMENT', default='development')

# Загружаем .env файл в зависимости от окружения
if ENVIRONMENT == 'production':
    env_file = BASE_DIR / '.env.production'
else:
    env_file = BASE_DIR / '.env'

environ.Env.read_env(env_file=env_file)

# Безопасность и ключевые настройки
SECRET_KEY = env('SECRET_KEY', default='fallback_secret_key')
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

# Проверка наличия ключевых настроек
if not SECRET_KEY:
    raise ValueError("SECRET_KEY не установлена в файле окружения")

# URL вашего сайта
SITE_URL = env('SITE_URL', default='http://127.0.0.1:8000')

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'search_service',
    'user_service',
    'property_service',
    'booking_service',
    'notifications_service',
    'analytics_service',
    'review_service',
]

SITE_ID = 1

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# URL конфигурация
ROOT_URLCONF = 'rentapp.urls'

# Шаблоны
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

# WSGI
WSGI_APPLICATION = 'rentapp.wsgi.application'

# Базы данных (используйте DATABASE_URL в продакшн)
DATABASES = {
    'default': env.db('DATABASE_URL', default=f'sqlite:///{BASE_DIR}/db.sqlite3'),
}

# Валидация паролей
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

# Языковые и временные настройки
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические и медиа файлы
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Настройки редиректа
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'user_dashboard'
LOGOUT_REDIRECT_URL = 'home'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки электронной почты
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='smtp.example.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', default=False)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default=None)
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default=None)
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='webmaster@localhost')

# Проверка настроек электронной почты
if not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD:
    raise ValueError("EMAIL_HOST_USER и EMAIL_HOST_PASSWORD должны быть установлены в окружении.")

# Настройки Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

# Настройки JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}

# Swagger settings
SWAGGER_SETTINGS = {
    'LOGIN_URL': 'account_login',
    'LOGOUT_URL': 'account_logout',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'none',
    'DEFAULT_MODEL_RENDERING': 'example',
}
