from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.db.models.functions import Lower
from .models import Product, Review, Category
from django.db.models import Avg, Count

from django.db.models import Avg
from django.contrib import messages
from django.db.models import Q



# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all().annotate(avg_rating=Avg('review__rating'))
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'rating':
                sortkey = 'avg_rating'
                direction = 'desc'

            if sortkey == 'category':
                sortkey = 'category__name'


            products = products.order_by(sortkey)

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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