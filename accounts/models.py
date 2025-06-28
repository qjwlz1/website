from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import random

class SneakerCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sneaker = models.ForeignKey("Sneaker", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.sneaker.name} - {self.quantity} шт."
    class Meta:
        unique_together = ('user', 'sneaker')

class SneakerFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    sneaker = models.ForeignKey("Sneaker", on_delete=models.CASCADE, related_name="favorited_by")

    def __str__(self):
        return f"{self.user.username} - {self.sneaker.name}"
    class Meta:
        unique_together = ('user', 'sneaker')

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
        
    )
def generate_random_id():
    return str(random.randint(10000, 99999))

    def __str__(self):
        return self.title