from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Categories, SubCategories, Products
from .serializers import (
    CategoriesSerializer,
    SubCategoriesSerializer,
    ProductsSerializer,
)


# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Categories": "/categories/",
        "SubCategories": "/subcategories/",
        "Products": "/products/",
    }
    return Response(api_urls)


@api_view(["GET"])
def categories(request):
    categories = Categories.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def subcategories(request, fk):
    subcategories = SubCategories.objects.filter(category=fk)
    serializer = SubCategoriesSerializer(subcategories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def products(request, fk):
    products = Products.objects.filter(subcategory=fk)
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)
