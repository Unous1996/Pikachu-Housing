from django.db import models
from provider.models import Provider
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class House(models.Model):
    name = models.CharField(max_length=32, )
    location = models.CharField(max_length=128, blank=True)
    price = models.IntegerField(default=0)
    cover_img = models.CharField(max_length=128, blank=True, default='')
    types = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=600, blank=True)
    provider = models.ForeignKey(Provider, blank=True, null=True)
    imgs = ArrayField(models.CharField(max_length=128, blank=True), size=100, default=[], blank=True)

    def __str__(self):
        return str(self.id) + ' (' + self.name + ')'
