from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product
from django.conf import settings


def all_products(request):
    """ View to return all products, sorting and search queries """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None
    currency_symbol = settings.CURRENCY_SYMBOL
    currency = settings.CURRENCY
    max_rating = [0, 1, 2, 3, 4]

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sort == 'rating':
                for product in products:
                    product.update_rating()

            if sortkey == 'name':
                sortkey == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            


            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error("Type something in the search bar!")
                return redirect(reverse('products'))

            if query == 'discounted':
                discounted_products = []
                for product in products:
                    if product.is_discounted():
                        discounted_products.append(product)
                products = discounted_products
            else:
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    current_sorting = f'{sort}-{direction}'

    context = {
        'products': products,
        'currency_symbol': currency_symbol,
        'currency': currency,
        'max_rating':  max_rating,
        'search_term': query,
        'current_sorting': current_sorting
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
    }

    return render(request, 'products/product_detail.html', context)
