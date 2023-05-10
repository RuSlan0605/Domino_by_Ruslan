from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from shop.models import *
from API.serializers import *

class ProductListPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination

class ProductAPIView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination

class CategoryAPIView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ProductListPagination

class ColorAPIView(generics.ListCreateAPIView):

    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    pagination_class = ProductListPagination

class SizeAPIView(generics.ListCreateAPIView):

    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    pagination_class = ProductListPagination

class CountryAPIView(generics.ListCreateAPIView):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = ProductListPagination

class BrandAPIView(generics.ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = ProductListPagination
