# drf_app/views.py
from rest_framework import generics, permissions, viewsets
from .models import Handbag, Brand
from .serializers import HandbagSerializer, BrandSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .util import get_brand_description
import logging

logger = logging.getLogger(__name__)

class HandbagList(generics.ListCreateAPIView):
    queryset = Handbag.objects.all()
    serializer_class = HandbagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        handbags = Handbag.objects.all()

        for handbag in handbags:            
            brand_name = handbag.brand.name
            brand_description = handbag.brand.description
            
            result = get_brand_description(brand_name, brand_description)

            if result:
                logger.info(f"Brand Description for {brand_name}: {result}")

        return handbags

class HandbagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Handbag.objects.all()
    serializer_class = HandbagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

class HandbagViewSet(viewsets.ModelViewSet):
    queryset = Handbag.objects.all()
    serializer_class = HandbagSerializer
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]