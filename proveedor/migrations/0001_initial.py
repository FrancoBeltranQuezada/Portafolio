# Generated by Django 3.0.6 on 2020-05-25 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prov',
            fields=[
                ('id_prov', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=30)),
            ],
        ),
    ]
