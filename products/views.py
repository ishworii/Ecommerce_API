from rest_framework import generics

from products.serializers import ProductSerializer
from products.models import Product
from products.permissions import IsAdmin, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
