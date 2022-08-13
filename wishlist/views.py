from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect

from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


def add_to_wishlist(request, item_id):
    """
    Add product to user's wishlist
    """

    profile = UserProfile.objects.get(user=request.user)
    product = Product.objects.get(pk=item_id)

    redirect_url = request.POST.get('redirect_url')

    if profile.wishlist.exists():
        wishlist = profile.wishlist.get()

        wishlist.products.add(product)

        messages.success(request, f'Added {product.name} to wishlist!')

    else:
        wishlist = Wishlist(user_profile=profile)
        wishlist.save()
        wishlist.products.add(product)

        messages.success(request, f'Added {product.name} to wishlist!')

    print(redirect_url)

    return redirect(request.META['HTTP_REFERER'])