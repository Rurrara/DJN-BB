from django.db import models

# Create your models here.

class Category(models.Model):
    name_category = models.CharField(max_length=256, unique=True)
    description_category = models.CharField(max_length=4096)

    def __str__(self):
        return self.name_category