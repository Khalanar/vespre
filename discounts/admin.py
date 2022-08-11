from django.contrib import admin
from .models import Discount


class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'amount',
        'is_active',
        'date_created',
    )

    ordering = ('-date_created',)

admin.site.register(Discount, DiscountAdmin)