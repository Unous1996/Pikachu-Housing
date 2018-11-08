# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from housing.models import House
from department.models import Department
from rest_framework import generics

# Create your models here.

class Distance(generics.ListCreateAPIView):
    house_id = models.ForeignKey(House, blank=False, null=False)
    department_id = models.ForeignKey(Department, blank=False, null=False)
    distance = models.FloatField(default=0, blank=False)
