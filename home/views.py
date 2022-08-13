from django.shortcuts import render, get_object_or_404
from products.models import Product


# Create your views here.
def index(request):
    """ View that returns the index page """
    products = Product.objects.all()

    context = {
        'products': products[:8],
    }
    
    return render(request, "home/index.html", context)

def about_us(request):
    template = 'home/about-us.html'
    context = {
    
    }

    return render(request, template, context)