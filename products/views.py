from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product
from .forms import ProductForm


def all_products(request):
    """ View to return all products, sorting and search queries """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None
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
        'search_term': query,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View that returns one product by its ID """
    product = get_object_or_404(Product, pk=product_id)
    max_rating = [0, 1, 2, 3, 4]

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
