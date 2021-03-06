from products.models import Product
from django.conf import settings


def global_context(request):

    featured_products = []

    products = Product.objects.all()

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
        'max_rating': max_rating
    }

    return context