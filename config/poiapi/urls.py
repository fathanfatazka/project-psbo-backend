from django.urls import path
from .views import PoiList, PoiDetail

urlpatterns = [
    path('pois/', PoiList.as_view()),
    path('pois/<int:pk>/', PoiDetail.as_view()),
]