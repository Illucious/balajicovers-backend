from instamojo_wrapper import Instamojo

from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from checkout.models import Order


api = Instamojo(
    api_key=settings.INSTAMOJO_API_KEY,
    auth_token=settings.INSTAMOJO_AUTH_TOKEN,
    endpoint="https://test.instamojo.com/api/1.1/",
)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def payment_request(request):
    order = Order.objects.get(id=request.data["order_id"])
    response = api.payment_request_create(
        amount=order.total,
        purpose="Order Payment",
        send_email=True,
        email=request.user.email,
        redirect_url="http://localhost:8000/api/payments/success",
    )

    payment_url = response["payment_request"]["longurl"]
    payment_request_id = response["payment_request"]["id"]

    order.order_id = payment_request_id
    order.save()



@api_view(["GET"])
def payment_successful(request):
    payment_request_id = request.GET.get("payment_request_id")
    payment_id = request.GET.get("payment_id")

    response = api.payment_request_payment_status(payment_request_id, payment_id)

    if response["payment_request"]["status"] == "Completed":
        order = Order.objects.get(order_id=payment_request_id)
        order.placed = True
        order.save()
        return Response({"message": "Payment Successful"})
    else:
        return Response({"message": "Payment Failed"})