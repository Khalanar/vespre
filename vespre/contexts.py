from products.models import Product


def global_context(request):

    featured_products = []

    products = Product.objects.all()

    for product in products:
        if product.is_discounted():
            featured_products.append(product)


    context={
        'featured_products': featured_products,
    }

    return context