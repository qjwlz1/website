# Generated by Django 5.1.1 on 2025-02-23 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_sneaker_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sneaker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sneaker_images/'),
        ),
    ]
