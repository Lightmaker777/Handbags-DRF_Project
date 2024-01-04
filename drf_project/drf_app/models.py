# drf_app/models.py
from django.db import models


class Handbag(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    seller = models.CharField(max_length=200)
    image_link = models.URLField() 
    