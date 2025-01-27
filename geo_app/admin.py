from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('name', 'coordinates')
