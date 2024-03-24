from django.db import models

# Create your models here.

class Airline(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    callsign = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=50)



