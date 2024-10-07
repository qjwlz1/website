from django.contrib import admin
from django.urls import path, include
from accounts import views  # Импортируем views из приложения accounts

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
<<<<<<< HEAD
    path('', views.index, name='index'),  # Главная страница
=======
    path('', views.index, name='index'),  # Главная страница (изменен путь на пустой для корневого URL)
>>>>>>> 5bee5fc3f7edd8a4056ecdd4163ed2a26f0b8d48
    path('login/', views.login_page, name='login'),  # Страница входа
    path('register/', views.register_page, name='register'),  # Страница регистрации
    path('logout/', views.logout_user, name='logout'),  # Выход
    path('accounts/', include('accounts.urls')),  # Подключение маршрутов для аккаунтов
]
