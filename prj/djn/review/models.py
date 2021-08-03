from django.db import models

from django.conf import settings
from item.models import Item

from datetime import datetime

# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='author_review_set')
    bought_item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, null=True)
    review_text = models.CharField(max_length=4096)
    rating = models.BooleanField(default=False)
    date_published= models.DateField(auto_now=True)
