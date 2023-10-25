from django.urls import path
from . import views


urlpatterns = [
    path("create-payment/", views.payment_request, name="payment-request"),
    path("success/", views.payment_successful, name="payment-successful"),
]
