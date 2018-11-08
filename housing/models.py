from django.db import models
from provider.models import Provider
# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=32, )
    location = models.CharField(max_length=128, blank=True)
    price = models.IntegerField(default=0)
    imgs_url = models.CharField(max_length=128, blank=True)
    types = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=600, blank=True)
    provider = models.ForeignKey(Provider, blank=True, null=True)

