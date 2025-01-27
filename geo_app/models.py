from django.contrib.gis.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.PointField()

    def __str__(self):
        return self.name

