
from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.generics import  RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from airline.models import Airline
from airline.serializers import AirlineDetailSerializer

class AirlineViewSet(viewsets.ViewSet):

    def retrieve(self, request):
        qs = Airline.objects.all()
        data = serialize("json", qs, fields=('name', 'callsign', 'founded_year', 'base_airport'))
        return HttpResponse(data, content_type="application/json")

    def save_airline(self, request):

        airline = Airline.objects.create( name=request.data['name'], callsign=request.data['callsign'], founded_year=request.data['founded_year'], base_airport=request.data['base_airport'] )
        airline.save()
        response = Response({"message": "created successfully"})

        return response



class AirLineGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineDetailSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

