from .models import *
from .serializers import *
from rest_framework import  generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import OrderingFilter

class RestaurantListAPIView(generics.ListAPIView):
    queryset = RestaurantList.objects.all()
    serializer_class = RestaurantListSerializer

class AboutRestaurantListAPIView(generics.ListAPIView):
    queryset = AboutRestaurant.objects.all()
    serializer_class = AboutRestaurantSerializer



class BestSellersListAPIView(generics.ListAPIView):
    queryset = BestSellers.objects.all()
    serializer_class = BestSellersSerializer


class MainMenuListAPIView(generics.ListAPIView):
    queryset = MainMenu.objects.all()
    serializer_class = MainMenuSerializer
    filter_backends = [DjangoFilterBackend]




class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer





class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price']


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class VisitRestaurantListAPIView(generics.ListAPIView):
    queryset = VisitRestaurant.objects.all()
    serializer_class = VisitRestaurantSerializer


class ModernInteriorListAPIView(generics.ListAPIView):
    queryset = ModernInterior.objects.all()
    serializer_class = ModernInteriorSerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
