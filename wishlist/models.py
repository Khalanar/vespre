from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """
    Class to create wishlists for users 
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=False, blank=False,
                                     related_name="wishlist")
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return f'{self.user_profile}\'s wishlist'
