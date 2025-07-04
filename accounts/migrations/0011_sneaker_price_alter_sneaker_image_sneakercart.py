# Generated by Django 5.1.1 on 2025-02-24 22:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_sneaker_size'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='sneaker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='SneakerCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('sneaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_cart', to='accounts.sneaker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'sneaker', 'size')},
            },
        ),
    ]
