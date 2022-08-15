from django.contrib import admin

from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """
    Class to register wislists to the django admin
    """
    list_display = ['user_profile']

admin.site.register(Wishlist, WishlistAdmin)
