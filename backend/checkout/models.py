from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

from store.models import Products


# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    pin_code = models.IntegerField(
        validators=[MaxValueValidator(999999), MinValueValidator(000000)]
    )
    phone = models.BigIntegerField()
    is_custom = models.BooleanField(default=False)
    name_on_cover = models.CharField(max_length=100, blank=True, null=True, default="")
    image = models.ImageField(
        upload_to="images/customize", blank=True, null=True, default=None
    )
    items = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    total = models.FloatField()
    payment_option = models.CharField(
        max_length=50, default="ONLINE", choices=[("COD", "COD"), ("ONLINE", "ONLINE")]
    )
    placed = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, blank=True, null=True, default=None)
