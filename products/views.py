from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.db.models.functions import Lower
from .models import Product, Review, Category, Favorite
from django.db.models import Avg

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from .forms import ProductForm, ReviewForm


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # anotate with average rating
    products = Product.objects.all().annotate(avg_rating=Avg('review__rating'))
    query = None
    categories = None
    sort = None
    direction = None

    # Handling favorite products for authenticated users
    if request.user.is_authenticated:
        # Annotate with favorite counts if the user is a superuser
        if request.user.is_superuser:
            products = products.annotate(favorites_count=Count('favorite'))
        # Get the list of favorite product IDs for the logged-in user
        favorite_ids = Favorite.objects.filter(
            user=request.user).values_list('product_id', flat=True)
    else:
        favorite_ids = []

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
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    product_list = []
    for product in products:
        product.is_favorite = False
        if request.user.is_authenticated:
            product.is_favorite = Favorite.objects.filter(
                user=request.user, product=product).exists()
        product_list.append(product)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'favorite_ids': favorite_ids
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    review_count = reviews.count()

    is_favorite = False  # Initialize is_favorite
    favorites_count = 0  # Initialize favorites count

    # Check user is authenticated & if product is in their favorites
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user, product=product).exists()

    # Superuser specific feature: count how many users favorited this product
    if request.user.is_superuser:
        favorites_count = Favorite.objects.filter(product=product).count()

    if review_count > 0:
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    else:
        average_rating = None

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'review_count': review_count,
        'average_rating': average_rating,
        'form': form,
        'is_favorite': is_favorite,
        'favorites_count': favorites_count
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
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')  # noqa
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
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')  # noqa
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


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been submitted.')
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'product': product})  # noqa


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=review.product.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form, 'review': review})  # noqa


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    product_id = review.product.id
    review.delete()
    messages.success(request, 'Your review has been deleted.')
    return redirect('product_detail', product_id=product_id)


@login_required
def add_to_favorites(request, product_id):
    """ Add a product to the user's favorites """

    product = get_object_or_404(Product, id=product_id)
    _, created = Favorite.objects.get_or_create(
        user=request.user, product=product)
    if created:
        messages.success(
            request, f'"{product.name}" has been added to your favorites!')
    else:
        messages.info(
            request, f'"{product.name}" is already in your favorites.')
    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_favorites(request, product_id):
    """ Remove a product from the user's favorites """

    product = get_object_or_404(Product, id=product_id)
    deleted, _ = Favorite.objects.filter(
        user=request.user, product=product).delete()

    if deleted:
        messages.success(
            request, f'"{product.name}" has been removed from your favorites.')
    else:
        messages.info(
            request, f'"{product.name}" was not found in your favorites.')
    return redirect('product_detail', product_id=product_id)


@login_required
def user_favorites(request):
    """ Display the user's favorite products """

    favorites = Favorite.objects.filter(user=request.user).values_list(
        'product', flat=True)
    favorite_products = Product.objects.filter(id__in=favorites)

    if request.user.is_superuser:
        favorite_products = favorite_products.annotate(
            favorites_count=Count('favorite'))

    if not favorite_products.exists():
        messages.info(request, "You haven't added any favorites yet.")

    context = {
        'products': favorite_products,
    }

    return render(request, 'products/products.html', context)
