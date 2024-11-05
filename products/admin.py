from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'brand',
        'description',
        'serie_number',
        'cost_price',
        'selling_price',
        'created_at',
        'updated_at'
    )
    search_fields = ('title', )
