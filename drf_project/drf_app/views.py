# drf_app/views.py
from rest_framework import generics, permissions, viewsets
from .models import Handbag, Brand
from .serializers import HandbagSerializer, BrandSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .util import get_brand_description
import logging
from rest_framework.exceptions import ValidationError
from django.utils.html import escape, strip_tags
from django.utils.text import slugify
from drf_yasg.utils import swagger_auto_schema
import django_filters
import django_filters.rest_framework as filters


logger = logging.getLogger(__name__)

class HandbagFilter(django_filters.FilterSet):
    price = filters.NumberFilter(field_name='price',lookup_expr='startswith')
    color = filters.CharFilter(field_name='color',lookup_expr='startswith')
    class Meta:
        model = Handbag
        fields = ['brand', 'price', 'color']

class HandbagList(generics.ListCreateAPIView):
    queryset = Handbag.objects.all()
    serializer_class = HandbagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]    
    filterset_class = HandbagFilter

    @swagger_auto_schema(operation_description='Retrieve a list of handbags')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description='Add another handbag')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        try :
            serializer.save()           
        except ValidationError as e:
            raise ValidationError(detail=e.detail)

    def get_queryset(self):
        handbags = Handbag.objects.all()

        for handbag in handbags:            
            brand_name = handbag.brand.name
            brand_description = handbag.brand.description
            
            result = get_brand_description(brand_name, brand_description)

            if result:
                logger.info(f"Brand Description for {brand_name}: {result}")

        return handbags
    
    def perform_create(self, serializer):
        # Validate and sanitize the data before creating the object

        data = serializer.validated_data

        # Example validation: Ensure the brand name is not empty
        brand_name = data.get('brand', {}).get('name')
        if not brand_name:
            raise ValidationError("Brand name cannot be empty.")

        # Example sanitization: Strip HTML tags from the description
        description = data.get('brand', {}).get('description', '')
        sanitized_description = strip_tags(description)

        # Example sanitization: Create a slug from the brand name
        slugified_brand_name = slugify(brand_name)

        # Update the data with sanitized values
        data['brand']['description'] = sanitized_description
        data['brand']['name'] = slugified_brand_name

        serializer.save()

class HandbagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Handbag.objects.all()
    serializer_class = HandbagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_description='Retrieve a handbag by ID')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description='Update a single handbag')
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description='Delete a handbag')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

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