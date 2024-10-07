from django.contrib import admin
from django.urls import path, include
from accounts import views  # Импортируем views из приложения accounts

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('', views.index, name='index'),  # Главная страница
    path('login/', views.login_page, name='login'),  # Страница входа
    path('register/', views.register_page, name='register'),  # Страница регистрации
    path('logout/', views.logout_user, name='logout'),  # Выход
    path('accounts/', include('accounts.urls')),  # Подключение маршрутов для аккаунтов
]
