from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Discount
from .forms import DiscountForm, ApplyDiscountForm


@login_required
def discounts(request):
    """
    View all currently existing discounts
    """
    discounts = Discount.objects.all()

    template = 'discounts/discounts.html'

    context = {
        'form': 'form',
        'discounts': discounts,
    }

    return render(request, template, context)


@login_required
def add_discount(request):
    """
    Add a new discount
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            discount = form.save()
            messages.info(request, 'Successfully created a discount!')
            return redirect(reverse('discounts'))
        else:
            messages.error(request, 'Failed to add product.\
                           Please ensure the form is valid.')
    else:
        form = DiscountForm()

    template = 'discounts/add_discount.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_discount(request, discount_id):
    """
    Delete specified discount
    """
    discount = get_object_or_404(Discount, pk=discount_id)
    discount.delete()
    return redirect(reverse('discounts'))


def apply_discount(request):
    """
    Check if discount exists and save it into session
    """
    form = ApplyDiscountForm(request.POST)

    try:
        discount = Discount.objects.get(code=form.data['code'])
        request.session['discount_id'] = discount.id
        messages.info(request, f'{discount.code} applied to your cart.')
    except Discount.DoesNotExist:
        request.session['discount_id'] = None
        messages.error(request, 'no discount with this code sorry')

    return redirect('view_cart')
