# Generated by Django 3.1 on 2020-08-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0025_auto_20200824_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=1000),
        ),
    ]