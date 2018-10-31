from django.db import models

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=32, )
    url = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
