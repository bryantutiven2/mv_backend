# Generated by Django 3.1 on 2020-08-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0010_auto_20200822_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='logo',
        ),
        migrations.AddField(
            model_name='camposanto',
            name='logo',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
    ]