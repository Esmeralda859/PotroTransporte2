# Generated by Django 2.1.5 on 2020-04-21 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potrotransporte', '0010_auto_20200421_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepagomembresia',
            name='Activo',
        ),
        migrations.RemoveField(
            model_name='membresia',
            name='FechaInicio',
        ),
        migrations.RemoveField(
            model_name='membresia',
            name='FechaTerminacion',
        ),
        migrations.AddField(
            model_name='detallepagomembresia',
            name='FechaInicio',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha Inicio'),
        ),
        migrations.AddField(
            model_name='detallepagomembresia',
            name='FechaTerminacion',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha Terminacion'),
        ),
    ]