from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from django.db.models import Avg

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to render product details"""
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    review_count = reviews.count()

    if review_count > 0:
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    else:
        average_rating = None

    context = {
        'product': product,
        'reviews': reviews,
        'review_count': review_count,
        'average_rating': average_rating
    }

    return render(request, 'products/product_detail.html', context)