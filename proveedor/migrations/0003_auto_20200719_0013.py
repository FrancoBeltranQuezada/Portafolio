# Generated by Django 3.0.8 on 2020-07-19 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20200603_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prov',
            name='nombre_proveedor',
            field=models.CharField(help_text='Ingrese nombre proveedor', max_length=30),
        ),
    ]
