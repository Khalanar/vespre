from django.db import models
from django.db.models.signals import post_save
# from reviews.models import Review

#FOR TESTING PURPOSES ONLY
import random

class Product(models.Model):
    ''' Model for product objects '''
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    compare_at_price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.SmallIntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    imageURL = models.URLField(null=True, blank=True)


    def __str__(self):
        return str(self.name.replace('VESPRE ', '').replace(' Tee', ''))

    def update_rating(self):
        ''' Get the average rating for this product '''

        rating_sum = 0
        reviews_count = 0
        _rating = 0

        print(f'Updating rating for {self.name}')

        for review in self.reviews.all():
            reviews_count += 1
            rating_sum += review.rating

        _rating = rating_sum / reviews_count if reviews_count > 0 else -1
        self.rating = _rating

        # self.save()

    def is_discounted(self):
        ''' Returns true if the product's price is lower than the product's compare_at_price '''
        if self.compare_at_price != 0:
            return self.price < self.compare_at_price
        
        return False

    def savings(self):
        ''' Returns savings in % '''
        if self.is_discounted():
            
            return str(100 - int(self.price * 100 / self.compare_at_price))
        else:
            return 'no savings'

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        print("product is saving")
        self.update_rating()