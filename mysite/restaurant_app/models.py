from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class RestaurantList(models.Model):
    headline = models.CharField(max_length=32)
    title = models.CharField(max_length=100)
    description = models.TextField()
    list_image = models.ImageField(upload_to='list_image')
    title_location = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    title_hotline = models.CharField(max_length=32)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.headline

class AboutRestaurant(models.Model):
    headline = models.CharField(max_length=32)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.headline

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(AboutRestaurant, on_delete=models.CASCADE, related_name='restaurant_images')
    restaurant_image = models.ImageField(upload_to='restaurant_image')

class BestSellers(models.Model):
    headline = models.CharField(max_length=32)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.headline

class SellerImage(models.Model):
    seller = models.ForeignKey(BestSellers, on_delete=models.CASCADE, related_name='seller_images')
    seller_image = models.ImageField(upload_to='seller_image')


class ModernInterior(models.Model):
    headline = models.CharField(max_length=32)

    def __str__(self):
        return self.headline

class InteriorImage(models.Model):
    interior = models.ForeignKey(ModernInterior, on_delete=models.CASCADE, related_name='interior_images')
    interior_image = models.ImageField(upload_to='interior_image')

class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=64)
    product_image= models.ImageField(upload_to='product_image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'{self.product_name} - {self.category}'

class ProductIngradient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ingradient')
    ingradient_name = models.CharField(max_length=32)

class ProductExtras(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_extras')
    extras_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ProductDrinks(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_drinks')
    drink_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class MainMenu(models.Model):
    headline = models.CharField(max_length=32)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.headline

class RestaurantAddress(models.Model):
    title = models.CharField(max_length=32)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class RestaurantTime(models.Model):
    title = models.CharField(max_length=32)
    day_range1 = models.CharField(max_length=64)
    open_time1 = models.TimeField()
    close_time1 = models.TimeField()
    day_range2 = models.CharField(max_length=64)
    open_time2 = models.TimeField()
    close_time2 = models.TimeField()

    def __str__(self):
        return self.title

class RestaurantContact(models.Model):
    title = models.CharField(max_length=42)
    phone_number = PhoneNumberField()
    mail = models.URLField()

    def __str__(self):
        return self.title

class VisitRestaurant(models.Model):
    headline = models.CharField(max_length=32)
    title = models.CharField(max_length=100)
    restaurant_address = models.OneToOneField(RestaurantAddress, on_delete=models.CASCADE)
    restaurant_time = models.OneToOneField(RestaurantTime, on_delete=models.CASCADE)
    restaurant_contact = models.OneToOneField(RestaurantContact, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline













