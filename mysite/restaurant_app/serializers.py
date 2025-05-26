from rest_framework import serializers
from .models import *


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantList
        fields = ['id', 'headline', 'title', 'description', 'list_image', 'title_location', 'address', 'title_hotline', 'phone_number']

class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ['id', 'restaurant_image']

class SellerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerImage
        fields = ['id', 'seller_image']



class InteriorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorImage
        fields = ['id', 'interior_image']

class AboutRestaurantSerializer(serializers.ModelSerializer):
    restaurant_images = RestaurantImageSerializer(many=True, read_only=True)
    class Meta:
        model = AboutRestaurant
        fields = ['id', 'headline', 'title', 'description', 'restaurant_images']


class BestSellersSerializer(serializers.ModelSerializer):
    seller_images = SellerImageSerializer(read_only=True, many=True)
    class Meta:
        model = BestSellers
        fields = ['id', 'headline', 'title', 'description', 'seller_images']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'description']


class MainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMenu
        fields = ['id', 'headline', 'title']


class ProductIngradientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIngradient
        fields = ['id', 'ingradient_name']

class ProductExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductExtras
        fields = ['id', 'extras_name', 'price']


class ProductDrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDrinks
        fields = ['id', 'drink_name', 'price']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    product_ingradient = ProductIngradientSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id', 'category', 'product_name', 'product_image', 'category', 'price', 'product_ingradient']



class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    product_ingradient = ProductIngradientSerializer(read_only=True, many=True)
    product_extras = ProductExtrasSerializer(read_only=True, many=True)
    product_drinks = ProductDrinksSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_image', 'category', 'price', 'product_ingradient', 'product_extras', 'product_drinks']


class ModernInteriorSerializer(serializers.ModelSerializer):
    interior_images = InteriorImageSerializer(read_only=True, many=True)
    class Meta:
        model = ModernInterior
        fields = ['id', 'headline', 'interior_images']


class RestaurantAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAddress
        fields = ['id', 'title', 'address']

class RestaurantContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantContact
        fields = ['id', 'title', 'phone_number', 'mail']

class RestaurantTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTime
        fields = ['id', 'title', 'day_range1', 'open_time1', 'close_time1', 'day_range2', 'open_time2', 'close_time2']


class VisitRestaurantSerializer(serializers.ModelSerializer):
    restaurant_address = RestaurantAddressSerializer(read_only=True)
    restaurant_time = RestaurantTimeSerializer(read_only=True)
    restaurant_contact = RestaurantContactSerializer(read_only=True)
    class Meta:
        model = VisitRestaurant
        fields = ['id', 'headline', 'title', 'restaurant_address', 'restaurant_time', 'restaurant_contact']


class CategoryDetailSerializer(serializers.ModelSerializer):
    menu_product = ProductSimpleSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'menu_product']