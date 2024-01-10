# drf_app/urls.py

from django.urls import path
from .views import HandbagList, HandbagDetail
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HandbagViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
    title = 'Handbags API',
    default_version = 'v1',
    description = 'API for handbags',
    terms_of_service = "https://www.google.com/policies/terms",
    contact = openapi.Contact(email="contact@handbagsapi.local"),
    license = openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[],
)

urlpatterns = [
    path('handbags/',HandbagList.as_view(), name='handbag-list'),
    path('handbags/<int:pk>/',HandbagDetail.as_view(), name='handbag-detail'),   
    path('openapi/',schema_view.without_ui(cache_timeout=0)),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
]
