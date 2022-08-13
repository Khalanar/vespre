from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings
from profiles.models import UserProfile


def global_context(request):

    featured_products = []

    products = Product.objects.all()

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        if profile.wishlist.exists():
            wishlist = profile.wishlist.get()
            print('wishlist exists ' + str(profile.wishlist.get()))
    
        else:
            print('wishlist DOES NOT exist')
            wishlist = None
    else:
        print('user not authed')

    for product in products:
        if product.is_discounted():
            featured_products.append(product)

    currency_symbol = settings.CURRENCY_SYMBOL
    currency = settings.CURRENCY

    max_rating = [0,1,2,3,4]

    context = {
        'featured_products': featured_products,
        'currency_symbol': currency_symbol,
        'currency': currency,
        'max_rating': max_rating,
        'wishlist': wishlist,
    }

    return context