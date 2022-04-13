from django.db import models
from products.models import Product
from user_management.models import User


class Offers(models.Model):
    seller = models.ForeignKey(User, related_name='offer_sellers', on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name='offer_buyer', on_delete=models.CASCADE)
    product_detail = models.ForeignKey(Product, related_name='products_detail', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_ofered = models.BooleanField(default=False)
    choices = [(1, "Accept"), (2, "Decline"), (3, "Pending")]
    status = models.IntegerField(default=0, choices=choices)
    new_price = models.FloatField(default=0.0)


class MyCart(models.Model):
    product = models.ForeignKey(Product, related_name='product_id', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
