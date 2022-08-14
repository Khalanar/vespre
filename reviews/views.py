from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import ReviewForm
from products.models import Product
from django.contrib import messages


def add_review(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)

    if request.POST:
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.info(request, 'Successfully added review!')
            product.update_rating()

            return redirect(reverse('home'))
    else:
        form = ReviewForm(initial={'product': product_id})

    template = 'reviews/add_review.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)