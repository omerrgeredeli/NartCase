# Generated by Django 5.0.3 on 2024-03-16 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('callsign', models.CharField(max_length=50)),
                ('founded_year', models.IntegerField()),
                ('base_airport', models.CharField(max_length=50)),
            ],
        ),
    ]
