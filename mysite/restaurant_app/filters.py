from .models import Product, Category
from django_filters import FilterSet


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
        }

class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category': ['exact'],
        }

