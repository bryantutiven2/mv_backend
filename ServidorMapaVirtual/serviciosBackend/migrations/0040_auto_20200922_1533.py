# Generated by Django 3.1 on 2020-09-22 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '__first__'),
        ('serviciosBackend', '0039_auto_20200920_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camposanto',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='web',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='red_social',
            name='link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='responsable_difunto',
            name='correo',
            field=models.EmailField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='responsable_difunto',
            name='parentezco',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='sector',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tipo_sepultura',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='email address'),
        ),
    ]
