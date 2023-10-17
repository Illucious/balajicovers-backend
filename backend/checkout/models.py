from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    checkout = models.BooleanField(default=False)
    total = models.FloatField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    pin_code = models.IntegerField(
        validators=[MaxValueValidator(999999), MinValueValidator(000000)]
    )
    phone = models.IntegerField(
        validators=[MaxValueValidator(9999999999), MinValueValidator(0000000000)]
    )

    is_custom = models.BooleanField(default=False)
    name_on_cover = models.CharField(max_length=100, blank=True, null=True, default="")
    image = models.ImageField(
        upload_to="images/customize", blank=True, null=True, default=None
    )

    items = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    total = models.FloatField()

    placed = models.BooleanField(default=False)
    payment_intent_id = models.CharField(max_length=100, blank=True, null=True, default="")
