from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView

from aircraft.models import AirCraft
from aircraft.serializers import AirCraftDetailSerializer


# Create your views here.

class CreateAirCraft(CreateAPIView):
    queryset = AirCraft.objects.all()
    serializer_class = AirCraftDetailSerializer


class GenericAirCraftView(RetrieveUpdateDestroyAPIView):
    queryset = AirCraft.objects.all()
    serializer_class = AirCraftDetailSerializer
    lookup_field = 'pk'

