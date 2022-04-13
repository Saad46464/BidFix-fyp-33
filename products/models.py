from django.db import models
from user_management.models import User
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)



class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_removed = models.BooleanField(default=False)


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
    condition = models.IntegerField(default=0)
    description = models.TextField(null=True)
    fixed_price = models.BooleanField(default=False)
    seller_name = models.ForeignKey(User, related_name='product_seller', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True, default='')
    start_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    expiry_at= models.DateTimeField(null=True, blank=True)
    location_name= models.CharField(max_length=255)    # location_long = models.TextField(null=True)
    lat = models.CharField(max_length=225)
    log = models.CharField(max_length=225)
    image = models.ImageField(
        _("image"), upload_to=upload_to)
    seller_id = models.ForeignKey(
        User, related_name='seller_id_name', on_delete=models.CASCADE)
    is_ofered = models.BooleanField(default=False)

#
# class ProductFile(models.Model):
#     product_id = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='media')
#
