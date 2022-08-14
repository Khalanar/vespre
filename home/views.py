from django.shortcuts import render
from products.models import Product


def index(request):
    """
    View that returns the index page
    """
    products = Product.objects.all()

    context = {
        'products': products[:8],
    }
    
    return render(request, "home/index.html", context)


def about_us(request):
    """
    View that returns the about us page
    """
    template = 'home/about-us.html'
    return render(request, template)


def policy_pages(request, template):
    """
    View that returns a policy page via a template
    specified by its stringname
    """
    template = f'home/{template}.html'
    return render(request, template)
