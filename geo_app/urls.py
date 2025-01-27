from django.urls import path
from .views import LocationListCreateAPIView

urlpatterns = [

    path('locations/', LocationListCreateAPIView.as_view(), name='location-list'),
]
