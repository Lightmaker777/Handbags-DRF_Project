from urllib import response
from rest_framework import generics, permissions, viewsets
from .models import Handbag
from .serializers import HandbagSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication

class HandbagList(generics.ListCreateAPIView):
    queryset = Handbag.objects.all()
    serializer_class = HandbagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

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
