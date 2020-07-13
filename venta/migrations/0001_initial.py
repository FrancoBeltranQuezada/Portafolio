# Generated by Django 3.0.6 on 2020-07-13 20:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicio', '0004_auto_20200709_2031'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_agregada', models.DateTimeField(auto_now=True)),
                ('servicio', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicio.Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_boleta', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de boleta')),
                ('servicios', models.ManyToManyField(to='venta.OrderItem')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
