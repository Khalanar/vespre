from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.conf import settings

# Create your views here.
def index(request):
    """ View that returns the index page """

    featured_products = [
        get_object_or_404(Product, id='1'),
        get_object_or_404(Product, id='2')
    ]
    currency_symbol = settings.CURRENCY_SYMBOL
    currency = settings.CURRENCY

    context = {
        'featured_products': featured_products,
        'currency_symbol': currency_symbol,
        'currency': currency
    }
    
    return render(request, "home/index.html", context)