# Generated by Django 3.1 on 2020-10-04 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0049_auto_20201003_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial_rosas',
            fields=[
                ('id_rosa', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('rosa', models.BooleanField(default=True)),
                ('id_difunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviciosBackend.difunto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]