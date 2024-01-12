# drf_app/models.py
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
class Handbag(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # Many handbags can belong to one brand( many-to-one relationship)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=255, default='Unknown')
    description = models.TextField()
    seller = models.CharField(max_length=200)
    image_link = models.URLField()
