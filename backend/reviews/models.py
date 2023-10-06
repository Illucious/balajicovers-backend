from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from store.models import Products

# Create your models here.


class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    review_title = models.CharField(max_length=100)
    review_text = models.CharField(max_length=500)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_title
