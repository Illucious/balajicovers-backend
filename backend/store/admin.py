from django.contrib import admin
from .models import Categories, SubCategories, Products

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_filter = (
        "category",
        "subcategory",
    )
    list_display = ("name", "category", "subcategory")


admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products, ProductsAdmin)
