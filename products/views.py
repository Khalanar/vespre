from django.shortcuts import render
from .models import Product
from django.conf import settings


def all_products(request):
    """ View to return all products, sorting and search queries """

    products = Product.objects.all()
    currency_symbol = settings.CURRENCY_SYMBOL
    currency = settings.CURRENCY
    max_rating = [0, 1, 2, 3, 4]

    context = {
        'products': products,
        'currency_symbol': currency_symbol,
        'currency': currency,
        'max_rating':  max_rating
    }

    return render(request, 'products/products.html', context)
