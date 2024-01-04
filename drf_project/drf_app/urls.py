from django.urls import path
from .views import HandbagList, HandbagDetail
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HandbagViewSet

router = DefaultRouter()
router.register(r'handbags', HandbagViewSet, basename='handbag')

urlpatterns = [
    path('handbags/',HandbagList.as_view()),
    path('handbags/<int:pk>/',HandbagDetail.as_view()),
    path('api/v1/', include(router.urls)),
]
