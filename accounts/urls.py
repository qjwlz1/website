from django.contrib import admin
from django.urls import path, include
from . import views  # Импортируем views из текущего приложения

urlpatterns = [
    path('admin/', admin.site.urls),  # Подключаем маршруты для админки
    path('login/', views.login_page, name='login'),  # Маршрут для страницы входа
    path('register/', views.register_page, name='register'),  # Маршрут для страницы регистрации
    path('logout/', views.logout_user, name='logout'),  # Добавляем маршрут для выхода
    path('', views.index, name='index'),  # Маршрут для главной страницы
    path('accounts/', include('accounts.urls')),  # Подключаем маршруты приложения accounts
]
