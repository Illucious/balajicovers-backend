from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer
from store.models import Products


# Create your views here.
class ProductReviewViewSet(ModelViewSet):
    ...
