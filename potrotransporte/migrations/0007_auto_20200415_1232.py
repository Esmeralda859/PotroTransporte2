# Generated by Django 2.1.5 on 2020-04-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potrotransporte', '0006_auto_20200415_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membresia',
            name='EstadoPago',
            field=models.CharField(choices=[('P', 'Pagado'), ('C', 'Cancelado'), ('E', 'Pendiente'), ('T', 'Cancelado Tiempo')], default='E', max_length=1),
        ),
    ]
