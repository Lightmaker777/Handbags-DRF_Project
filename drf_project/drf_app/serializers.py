from rest_framework import serializers
from .models import Handbag


class HandbagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Handbag
        fields = '__all__'
     
