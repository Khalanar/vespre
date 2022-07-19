from django.db import models


class Product(models.Model):
    ''' Model for product objects '''
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    compare_at_price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    imageURL = models.URLField(null=True, blank=True)
    
    #add reviews to model once they are created
    #reviews = models.ForeignKey(Reviews, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')

    def __str__(self):
        return str(self.name)

    def get_rating(self):
        ''' Get the average rating for this product '''
        rating = 0

        return rating
    
    def has_discount(self):

        return self.price < self.compare_at_price
