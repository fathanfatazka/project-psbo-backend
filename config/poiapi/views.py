from django.shortcuts import render
from rest_framework import generics
from .models import PointOfInterest
from .serializers import PointOfInterestSerializer

class PoiList(generics.ListAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer

class PoiDetail(generics.RetrieveAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer