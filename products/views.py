from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Product, Review, Category


from django.db.models import Avg
from django.contrib import messages
from django.db.models import Q



# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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