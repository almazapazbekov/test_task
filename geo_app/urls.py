from django.urls import path
from .views import LocationListCreateAPIView, AddressLocationListCreateAPIView

urlpatterns = [

    path('locations/', LocationListCreateAPIView.as_view(), name='location-list'),
    path('address-locations/', AddressLocationListCreateAPIView.as_view(), name='address-location-list'),
]
