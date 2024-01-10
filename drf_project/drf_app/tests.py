# drf_app/tests.py
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.utils.text import slugify
from django.urls import reverse
from .models import Handbag, Brand
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class HandbagTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            'admin','admin@test.py','testpassword'
        )
        self.token = Token.objects.create(user = self.admin_user)
        self.user = User.objects.create_user("user", "admin@test.com", "testpassword")
        self.user_token = Token.objects.create(user=self.user)
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
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post(self.url, self.handbag_data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Handbag.objects.count(), 1)
        self.assertEqual(Handbag.objects.get().name, 'TestHandbag')

    def test_get_handbag_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    

