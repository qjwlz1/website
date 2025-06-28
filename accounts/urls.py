from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('sneakers/red/', views.sneaker_red, name='red'),
    path('sneakers/green/', views.sneaker_green, name='green'),
    path('sneakers/orange/', views.sneaker_orange, name='orange'),
    path('sneakers/yellow/', views.sneaker_yellow, name='yellow'),
    path('sneakers/black/', views.sneaker_black, name='black'),
    path('sneakers/blue/', views.sneaker_blue, name='blue'),
    path('add_to_sneakersmarks/<str:color>/', views.add_to_sneakersmarks, name='add_to_sneakersmarks'),
    path('toggle_favorite/<str:sneaker_color>/', views.toggle_favorite, name='toggle_favorite'),
    path('cart/', views.cart, name='cart'),  # Страница корзины
    path('toggle_cart/<str:sneaker_color>/', views.toggle_cart, name='toggle_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),  # Новый путь для очистки корзины
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)