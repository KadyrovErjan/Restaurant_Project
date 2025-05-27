
from django.urls import path, include
from rest_framework import routers
from .views import *

routers = routers.SimpleRouter()


urlpatterns = [
    path('', include(routers.urls)),

    path('list/', RestaurantListAPIView.as_view(), name='restaurant_list'),

    path('about/', AboutRestaurantListAPIView.as_view(), name='about_list'),

    path('seller/', BestSellersListAPIView.as_view(), name='best_list'),

    path('menu/', MainMenuListAPIView.as_view(), name='menu_list'),

    path('visit/', VisitRestaurantListAPIView.as_view(), name='visit_list'),

    path('modern/', ModernInteriorListAPIView.as_view(), name='modern_list'),

    path('category/', CategoryListAPIView.as_view(), name='category_list'),

    path('categories/', CategoryDetailAPIView.as_view(), name='category_detail'),

    path('product/', ProductListAPIView.as_view(), name='product_list'),

    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),

]
