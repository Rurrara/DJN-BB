from django.db import models
from django.contrib.auth.models import AbstractUser

from item.models import Item

# Create your models here.

class User(AbstractUser):
    contact_telephone = models.CharField(max_length=10, blank=True)
    watched_items = models.ManyToManyField(Item, related_name="item_list", blank=True)
    balance = models.IntegerField(default=0)
