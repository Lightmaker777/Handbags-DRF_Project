# drf_app/serializers.py
from rest_framework import serializers
from .models import Handbag, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class HandbagSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()  # Use BrandSerializer for the 'brand' field

    class Meta:
        model = Handbag
        fields = '__all__'

    def create(self, validated_data):
        brand_data = validated_data.pop('brand', None)
        
        brand_instance, _ = Brand.objects.get_or_create(**brand_data)
        validated_data['brand'] = brand_instance

        handbag = Handbag.objects.create(**validated_data)
        return handbag
     
