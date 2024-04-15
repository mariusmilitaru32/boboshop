from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_key, item_data in bag.items():
        if isinstance(item_data, dict):
            product_id = item_data.get('product_id', None)
            if product_id:
                product = get_object_or_404(Product, pk=product_id)
                total += item_data['quantity'] * Decimal(product.price)
                product_count += item_data['quantity']
                bag_items.append({
                    'item_key': item_key,
                    'quantity': item_data['quantity'],
                    'product': product,
                    'size': item_data.get('size', None),
                })
            else:
                # Handle the case where 'product_id' is not present in item_data
                pass
        else:
            product = get_object_or_404(Product, pk=item_key)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_key': item_key,
                'quantity': item_data,
                'product': product,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context