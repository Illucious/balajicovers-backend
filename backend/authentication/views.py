from rest_framework import status

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        user = User.objects.get(username=serializer.data["username"])
        token = Token.objects.create(user=user)
        return Response(
            {"token": token.key, "user": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    try:
        user = User.objects.get(username=request.data["username"])
        print("passed")
        if user.check_password(request.data["password"]):
            token, _ = Token.objects.get_or_create(
                user=user
            )  # note the tuple unpacking
            serializer = UserSerializer(instance=user)
            return Response(
                {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
            )
        else:
            raise User.DoesNotExist
    except User.DoesNotExist:
        return Response(
            {"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST
        )  # changed the error message
