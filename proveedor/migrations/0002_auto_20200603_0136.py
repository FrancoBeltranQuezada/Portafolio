# Generated by Django 3.0.6 on 2020-06-03 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prov',
            options={'ordering': ['nombre_proveedor']},
        ),
    ]
