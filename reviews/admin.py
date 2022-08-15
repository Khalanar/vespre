from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Class to display reviews in django admin
    """
    list_display = (
        'rating',
        'comment',
        'name',
        'product',
        'date_created',
    )

    ordering = ('-date_created',)


admin.site.register(Review, ReviewAdmin)
