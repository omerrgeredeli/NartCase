from rest_framework import serializers

from aircraft.models import AirCraft


class AirCraftDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirCraft
        fields = ('__all__')