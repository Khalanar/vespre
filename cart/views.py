from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.conf import settings

# Create your views here.
def view_cart(request):
    """ View that returns the cart page """

    featured_products = []

    products = Product.objects.all()

    for product in products:
        if product.is_discounted():
            featured_products.append(product)
            print('found a discounted one')

    currency_symbol = settings.CURRENCY_SYMBOL
    currency = settings.CURRENCY

    max_rating = [0,1,2,3,4]

    context = {
        'products': products[:8],
        'featured_products': featured_products,
        'currency_symbol': currency_symbol,
        'currency': currency,
        'max_rating': max_rating
    }
    
    return render(request, "cart/cart.html", context)