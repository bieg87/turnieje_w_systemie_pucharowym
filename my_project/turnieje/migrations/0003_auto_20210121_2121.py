# Generated by Django 3.0 on 2021-01-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnieje', '0002_turnieje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnieje',
            name='date_of_start',
            field=models.DateField(),
        ),
    ]
