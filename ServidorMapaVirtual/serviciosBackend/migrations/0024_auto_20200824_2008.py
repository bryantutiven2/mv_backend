# Generated by Django 3.1 on 2020-08-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0023_auto_20200824_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='email address'),
        ),
    ]