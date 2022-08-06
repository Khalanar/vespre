from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Product


class Review(models.Model):
    """
    Model for product reviews
    """
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)], null=False, blank=False)
    comment = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, default='Anonymous', null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        return name and date
        """
        return f'Reviewed by {self.name} on {self.date_created}'
