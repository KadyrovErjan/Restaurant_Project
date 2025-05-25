from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(RestaurantList)
class RestaurantListTranslationOptions(TranslationOptions):
    fields = ('headline', 'title', 'description', 'title_location', 'address', 'title_hotline')


@register(AboutRestaurant)
class AboutRestaurantTranslationOptions(TranslationOptions):
    fields = ('headline', 'title', 'description')


@register(BestSellers)
class BestSellersTranslationOptions(TranslationOptions):
    fields = ('headline', 'title', 'description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')


@register(ProductIngradient)
class ProductIngradientTranslationOptions(TranslationOptions):
    fields = ('ingradient_name',)

@register(ProductExtras)
class ProductExtrasTranslationOptions(TranslationOptions):
    fields = ('extras_name',)

@register(ProductDrinks)
class ProductDrinksTranslationOptions(TranslationOptions):
    fields = ('drink_name',)

@register(MainMenu)
class MainMenuTranslationOptions(TranslationOptions):
    fields = ('headline', 'title' )

@register(ModernInterior)
class ModernInteriorTranslationOptions(TranslationOptions):
    fields = ('headline', )

@register(VisitRestaurant)
class VisitRestaurantTranslationOptions(TranslationOptions):
    fields = ('headline', 'title')

@register(RestaurantAddress)
class RestaurantAddressTranslationOptions(TranslationOptions):
    fields = ('title', 'address')

@register(RestaurantTime)
class RestaurantTimeTranslationOptions(TranslationOptions):
    fields = ('title', 'day_range1', 'day_range2')

@register(RestaurantContact)
class RestaurantContactTranslationOptions(TranslationOptions):
    fields = ('title', )





