from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_app.views import HandbagViewSet

router = DefaultRouter()
router.register(r'handbags', HandbagViewSet, basename='handbag')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/',include('drf_app.urls')),
]
