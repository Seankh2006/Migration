# Generated by Django 4.1.3 on 2023-02-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights2', '0002_rename_newflight_flight2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='Passenger', to='flights2.flight')),
            ],
        ),
    ]
