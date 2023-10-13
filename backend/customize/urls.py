from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Customize
from .serializers import CustomizeSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def customize(request):
    ...
