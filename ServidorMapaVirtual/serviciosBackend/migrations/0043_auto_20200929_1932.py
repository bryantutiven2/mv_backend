# Generated by Django 3.1 on 2020-09-30 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0042_auto_20200923_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camposanto',
            name='logo',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='logos'),
        ),
    ]
