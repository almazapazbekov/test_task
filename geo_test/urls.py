from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('geo_app.urls')),  # подключаем urls вашего приложения
]
