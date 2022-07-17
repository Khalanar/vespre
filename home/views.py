from django.shortcuts import render

# Create your views here.
def index(request):
    """ View that returns the index page """
    featured_products = ['product1', 'product2']
    context = {
        'featured_products': featured_products,
    }
    return render(request, "home/index.html", context)