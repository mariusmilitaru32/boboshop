from django.contrib import admin
from .models import Product, Category, Review, Favorite


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )
    
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'subject',
        'review',
        'rating',
        'created_at',
    )

class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)