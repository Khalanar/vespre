from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Discount
from .forms import DiscountForm

# Create your views here.

@login_required
def discounts(request):

    discounts = Discount.objects.all()

    template = 'discounts/discounts.html'

    context = {
        'form': 'form',
        'discounts': discounts,
    }

    return render(request, template, context)

@login_required
def add_discount(request):
    """ Add a new discount """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            discount = form.save()
            messages.success(request, 'Successfully created a discount!')
            return redirect(reverse('discounts'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = DiscountForm()
        
    template = 'discounts/add_discount.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_discount(request, discount_id):
    print("DELETING")
    discount = get_object_or_404(Discount, pk=discount_id)
    discount.delete()
    print("DELETING")
    return redirect(reverse('discounts'))
