from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("categories/", views.categories, name="categories"),
    path("subcategories/<str:fk>/", views.subcategories, name="subcategories"),
    path("product/<str:pk>/", views.products, name="products"),
    # wishlist
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wishlist/delete/<str:pk>/", views.wishlist_delete, name="wishlist"),
]
