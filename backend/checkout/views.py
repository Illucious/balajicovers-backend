from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Cart, Order
from store.models import Products
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
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def place_order(request):
    cart = Cart.objects.get(user=request.user)
    if cart is not None:
        cart.checkout = True
        cart.save()
        items = cart.items

        total = 0
        for item in items:
            product = Products.objects.get(id=item)
            total += product.price

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, items=items, total=total)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        item = Products.objects.get(id=request.data["items"])
        total = item.price
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, items=item, total=total)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
