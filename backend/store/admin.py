from django.contrib import admin
from .models import Categories, SubCategories, Products

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_filter = (
        "category",
        "subcategory",
    )
    list_display = ("name", "category", "subcategory")


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)


class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(SubCategories, SubCategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
