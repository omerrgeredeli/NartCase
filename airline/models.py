from django.db import models

# Create your models here.

class Airline(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    callsign = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=50)

class Aircraft(models.Model):
    manufacturer_serial_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    operator_airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    number_of_engines = models.IntegerField()

