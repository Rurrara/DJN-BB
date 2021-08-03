from django.db import models

from django.conf import settings
from category.models import Category

from djn_bb.storage_backends import PublicMediaStorage

from datetime import datetime

# Create your models here.

def get_picture_path(instance, filename):
    item_id = instance.id
    return f'{item_id}_{filename}'

class Item(models.Model):
    title_item = models.CharField(max_length=256)
    description_item = models.CharField(max_length=65536)
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='seller_item_set')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='buyer_item_set')
    categories = models.ManyToManyField(Category, related_name="category_list", blank=True)
    date_added = models.DateField(auto_now=True)
    date_edited = models.DateField(auto_now=True)
    ended = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    picture = models.ImageField('Picture', null=True, blank=True, storage=PublicMediaStorage())
