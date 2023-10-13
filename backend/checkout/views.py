from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Cart, Order
from .serializers import CartSerializer, OrderSerializer

# Create your views here.


# cart views
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_cart(request):
    cart = Cart.objects.get(user=request.user)
    serializer = CartSerializer(Cart, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.delete()
    return Response("Cart Deleted")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    cart = Cart.objects.get(user=request.user)
    serializer = CartSerializer(Cart, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# order views here
