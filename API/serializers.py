from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from shop.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'product_name',
            'description',
            'main_img',
            'image1',
            'image2',
            'image3',
            'price',
            'stock',
            'made',
            'category',
            'size',
            'color',
            'brand',
        )
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['made'] = instance.made.country_name
        response['category'] = instance.category.category_name
        response['size'] = instance.size.size_name
        response['color'] = instance.color.color_name
        response['brand'] = instance.brand.brand_name

        return response


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'category_name',
            'category_img',
            'category_desc',
            'slug',
        )

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'id',
            'color_name',
        )       

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'id',
            'size_name',
        )

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'country_name',
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'brand_name',
        )
