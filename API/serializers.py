from rest_framework import serializers
from shop.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            '__all__'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            '__all__'
        )

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            '__all__'
        )       

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            '__all__'
        )

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            '__all__'
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            '__all__'
        )
