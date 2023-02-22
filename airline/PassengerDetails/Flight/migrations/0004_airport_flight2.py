# Generated by Django 4.1.3 on 2023-02-01 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Flight', '0003_passenger_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Flight2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Arrivals', to='Flight.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Departures', to='Flight.airport')),
            ],
        ),
    ]
