from django.contrib import admin
from .models import CustomUser  # Пример: добавляем модель пользователя

# Регистрируем модель в админке
admin.site.register(CustomUser)
