from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "POI API",
        default_version = "v1",
        description="API for point of interest in IPB that potentially to be crowded",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="fahrury_rdd27@apps.ipb.ac.id"),
        license=openapi.License(name="BSD License"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poi/v1/', include('poiapi.urls')),
    # for documentation
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'
    ),
]
