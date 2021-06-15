from django.shortcuts import render
from rest_framework import generics
from .models import PointOfInterest
from .serializers import PointOfInterestSerializer

class PoiList(generics.ListCreateAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer

class PoiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer