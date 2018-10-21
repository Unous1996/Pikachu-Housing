from django.db import models

# Create your models here.


class House(models.Model):
    name = models.CharField(max_length=32, )
    location = models.CharField(max_length=32, blank=True)
    price = models.IntegerField(default=0)
    imgs_url = models.CharField(max_length=64, blank=True)
    types = models.CharField(max_length=32, blank=True)
