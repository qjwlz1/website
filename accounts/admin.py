from django.contrib import admin
from .models import CustomUser
admin.site.register(CustomUser)
from .models import Sneaker

admin.site.register(Sneaker)