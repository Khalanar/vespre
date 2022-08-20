from django.contrib import admin
from .models import Discount


class DiscountAdmin(admin.ModelAdmin):
    """
    Class to create the view for discounts in the django admin
    """
    list_display = (
        'name',
        'code',
        'amount',
        'type',
        'is_active',
        'date_created',
    )
    prepopulated_fields = {'code': ('name',)}

    ordering = ('-date_created',)

admin.site.register(Discount, DiscountAdmin)
