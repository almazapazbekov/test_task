from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer, AddressLocationSerializer

class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer



class AddressLocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = AddressLocationSerializer

