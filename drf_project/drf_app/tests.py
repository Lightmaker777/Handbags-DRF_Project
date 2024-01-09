# drf_app/tests.py
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Handbag, Brand

class HandbagTests(APITestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="TestBrand", description="Test Description")
        self.handbag_data = {
            "brand": {"name": "TestBrand", "description": "Brand Description"},
            "name": "TestHandbag",
            "price": "92.95",
            "description": "Test Description",
            "seller": "TestSeller",
            "image_link": "https://example.com/image.jpg",
        }
        self.url = reverse('handbag-list')

    def test_create_handbag(self):
        response = self.client.post(self.url, self.handbag_data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Handbag.objects.count(), 1)
        self.assertEqual(Handbag.objects.get().name, 'TestHandbag')

    def test_get_handbag_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    

