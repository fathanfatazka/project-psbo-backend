from rest_framework import serializers
from .models import PointOfInterest

class PointOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'place_name', 'location',)
        model = PointOfInterest
