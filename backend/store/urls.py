from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("categories/", views.categories, name="categories"),
    path("subcategories/<str:fk>/", views.subcategories, name="subcategories"),
    path("categoryproducts/<str:fk>", views.category_products, name="categoryproducts"),
    path("product/<str:pk>/", views.products, name="products"),
]
