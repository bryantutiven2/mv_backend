# Generated by Django 3.1 on 2020-08-22 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0011_auto_20200822_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='punto_geolocalizacion',
            old_name='longintud',
            new_name='longitud',
        ),
    ]
