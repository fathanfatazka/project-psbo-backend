# from django.db import models
# from django.db.models.base import Model
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class PointOfInterest(models.Model):
    place_name = models.CharField(max_length=30, null=False, blank=False)
    location = models.PointField(geography=True, default=Point(0.0, 0.0))

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y

    def __str__(self):
        return self.place_name