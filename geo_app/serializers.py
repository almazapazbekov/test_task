from rest_framework import serializers
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'coordinates']



geolocator = Nominatim(user_agent="myGeocoder")

class AddressLocationSerializer(serializers.ModelSerializer):
    address = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Location
        fields = ['id', 'name', 'coordinates', 'address']

    def create(self, validated_data):
        # Геокодируем адрес в координаты
        address = validated_data.pop('address', None)
        if address:
            location = geolocator.geocode(address)
            if location:
                validated_data['coordinates'] = Point(location.longitude, location.latitude)
        return super().create(validated_data)
