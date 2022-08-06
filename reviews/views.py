from django.shortcuts import render, get_object_or_404
from .forms import ReviewForm
from products.models import Product

def add_review(request, product_id):
    if request.GET:
        form = ReviewForm(initial={'product': product_id})
        product = get_object_or_404(Product, id=product_id)
    else:
        form = ReviewForm(initial={'product': product_id})
        product = get_object_or_404(Product, id=product_id)


    template = 'reviews/add_review.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)