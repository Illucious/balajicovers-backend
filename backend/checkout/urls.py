from django.urls import path

from . import views


urlpatterns = [
    path("cart/", views.get_cart, name="get_cart"),
    path("cart/delete/", views.delete_cart, name="delete_cart"),
    path("cart/add/", views.add_to_cart, name="add_to_cart"),
    path("order/", views.place_order, name="place_order"),
]
