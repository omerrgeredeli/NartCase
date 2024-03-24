from django.db import models

from airline.models import Airline


# Create your models here.
class AirCraft(models.Model):
    manufacturer_serial_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    operator_airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    number_of_engines = models.IntegerField()
