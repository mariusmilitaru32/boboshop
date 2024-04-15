from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')

    bag = request.session.get('bag', {})

    # Create a unique key for the product-size combination
    product_size_key = f"{item_id}_{size}" if size else item_id

    if product_size_key in bag:
        bag[product_size_key]['quantity'] += quantity
    else:
        product = get_object_or_404(Product, pk=item_id)
        bag[product_size_key] = {
            'quantity': quantity,
            'size': size,
            'product_id': product.id,
            'price': str(product.price),
        }

    request.session['bag'] = bag
    return redirect(redirect_url)