from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Set Product settings in admin view
    """
    list_display = (
        'id',
        'name',
        'price',
        'compare_at_price',
    )
    ordering = ('id',)

admin.site.register(Product, ProductAdmin)
