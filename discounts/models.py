from django.db import models


DISCOUNT_TYPE_CHOICES = (
    ('1', "%"),
    ('2', "€")
)


class Discount(models.Model):
    """
    Model for discounts
    """
    name = models.CharField(max_length=32, default='My_discount_code',
                            null=False, unique=True)
    code = models.CharField(max_length=32, null=False, unique=False)
    type = models.CharField(max_length=16, choices=DISCOUNT_TYPE_CHOICES,
                            null=False, blank=False, default=1)
    amount = models.PositiveSmallIntegerField(default=10, null=False,
                                              blank=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
