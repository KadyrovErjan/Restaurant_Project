from .models import Product, MainMenu
from django_filters import FilterSet


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
        }
