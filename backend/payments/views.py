from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import stripe

from .utilities import send_success_email
from checkout.models import Order




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    amount = int(Order.objects.get(user=request.user, placed=False).total())

    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='inr',
        )
        return Response({"client_secret": intent["client_secret"]}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def payment_successful(request):
    payment_intent_id = request.data.get("paymentIntentId")
    if payment_intent_id:
        Order.objects.filter(user=request.user, placed=False).update(placed=True)
        Order.objects.filter(user=request.user, placed=False).update(payment_intent_id=payment_intent_id)
        
        send_success_email(payment_intent_id)
        
        return Response({"message": "Payment successful"}, status=status.HTTP_200_OK)
    return Response({"error": "No payment intent id provided"}, status=status.HTTP_400_BAD_REQUEST)