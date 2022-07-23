from django.shortcuts import render, get_object_or_404
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

def product_detail(request, product_id):
    """ View that returns one product by its ID """
    product = get_object_or_404(Product, pk=product_id)
    currency_symbol = settings.CURRENCY_SYMBOL
    currency = settings.CURRENCY
    max_rating = [0, 1, 2, 3, 4]

    context = {
        'product': product,
        'currency_symbol': currency_symbol,
        'currency': currency,
        'max_rating': max_rating,
        # 'template_name': 
    }

    return render(request, 'products/product_detail.html', context)

