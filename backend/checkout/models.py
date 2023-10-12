from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    checkout = models.BooleanField(default=False)
    total = models.FloatField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    items = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    total = models.FloatField()