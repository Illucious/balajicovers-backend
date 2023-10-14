from django.urls import path
from .views import product_review_list_create

urlpatterns = [
    path(
        "product/<int:product_id>/reviews/",
        product_review_list_create,
        name="product-review-list-create",
    ),
]
