# Generated by Django 4.1.3 on 2023-02-21 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flight', '0004_airport_flight2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Passenger',
        ),
    ]
