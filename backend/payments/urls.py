from django.urls import path
from . import views


urlpatterns = [
    path("create-payment/", views.create_payment, name="create-payment"),
    path("payment-successful/", views.payment_successful, name="payment-successful"),
]
