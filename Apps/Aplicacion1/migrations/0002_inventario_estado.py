# Generated by Django 2.2.6 on 2019-11-01 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
    ]
