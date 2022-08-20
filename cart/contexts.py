from django.shortcuts import get_object_or_404
from products.models import Product
from discounts.models import Discount


def cart_contents(request):
    cart_items = []
    subtotal = 0
    total = 0
    total_discounted = 0
    discount_id = request.session.get('discount_id')

    if discount_id:
        discount = Discount.objects.get(pk=discount_id)
    else:
        discount = False

    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            subtotal += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, item_data in item_data['items_by_size'].items():
                subtotal += item_data * product.price
                product_count += item_data
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': size,
                })

            if discount:
                if discount.type == '1':
                    total_discounted = (subtotal * discount.amount / 100)
                elif discount.type == '2':
                    total_discounted = discount.amount

                total = subtotal - total_discounted
            else:
                total = subtotal

            if total < 0:
                total = 0

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'discount': discount,
        'total_discounted': total_discounted,
        'total': total,
        'product_count': product_count
    }

    return context
