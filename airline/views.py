from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from airline.models import Airline
from airline.serializers import AirlineDetailSerializer
from airline.models import Aircraft
from airline.serializers import AircraftDetailSerializer



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.


def index2(request):
    return HttpResponse("buda bizim index.")


class CreateAirline(CreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineDetailSerializer

class CreateAirCraft(CreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftDetailSerializer

class GetUpdateAirline(RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineDetailSerializer
    lookup_field = 'pk'

class UpdateAirline(UpdateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineDetailSerializer
    lookup_field = 'pk'

class GetUpdateAircraft(RetrieveUpdateDestroyAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftDetailSerializer
    lookup_field = 'pk'


class AirlineListView(ListAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineDetailSerializer



"""

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
    def get_object(self):
        obj = get_object_or_404(Airline, pk=self.kwargs["pk"])
        return obj
"""

