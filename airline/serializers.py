from rest_framework import serializers

from airline.models import Airline


class AirlineDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airline
        fields = ('__all__')

