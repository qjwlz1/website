import os
from pathlib import Path

# Путь к корневой директории проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ проекта
SECRET_KEY = 'your-secret-key'  # Убедитесь, что у вас установлен реальный секретный ключ

# Включаем режим отладки для разработки (выключить в продакшене)
DEBUG = True  # Для развертывания в продакшене следует установить False

# Хосты, с которых разрешён доступ
ALLOWED_HOSTS = ['*']

# Установленные приложения (включаем наше приложение 'accounts')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # Ваше приложение
]

# Мидлвары (обработчики запросов)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Главный файл маршрутов проекта
ROOT_URLCONF = 'website.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'accounts/templates'],  # Путь к папке с шаблонами
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

# Настройки базы данных (по умолчанию SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Настройки авторизации
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

# Язык и часовой пояс
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JavaScript, изображения)

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Adjust this path based on where your static files are stored


# Медиа файлы (если используешь загрузку файлов)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
