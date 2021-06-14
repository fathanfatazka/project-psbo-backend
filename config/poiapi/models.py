# from django.db import models
# from django.db.models.base import Model
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class PointOfInterest(models.Model):
    place_name = models.CharField(max_length=30, null=False, blank=False)
    location = models.PointField(geography=True, default=Point(106.7264194085899, -6.555760409044816))
    current_visitors = models.IntegerField(default=0, blank=False)
    peak_hours = models.BooleanField(default=False, blank=False)

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y

    def __str__(self):
        return self.place_name