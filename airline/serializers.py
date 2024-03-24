from rest_framework import serializers

from airline.models import Airline
from airline.models import Aircraft


class AirlineDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airline
        fields = ('__all__')

class AircraftDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aircraft
        fields = ('__all__')