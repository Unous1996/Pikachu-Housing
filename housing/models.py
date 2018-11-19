from django.db import models
from provider.models import Provider
import provider.models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from assist import *
# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=128,)
    location = models.CharField(max_length=128, blank=True)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cover_img = models.CharField(max_length=512, blank=True, default='')
    types = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    provider = models.ForeignKey(Provider, blank=True, null=True)
    imgs_url = ArrayField(models.CharField(max_length=512, blank=True), size=25, default=[], blank=True)
    latitude = models.FloatField(blank=True, null=True, default=0, validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.FloatField(blank=True, null=True, default=0, validators=[MaxValueValidator(180), MinValueValidator(-180)])

    def __str__(self):
        return str(self.id) + ' (' + self.name + ')'


    def save(self, **kwargs):
        if not self.pk:
            create = True
        else:
            create = False
            pk_val = self.pk

        super(House, self).save(**kwargs)
        print('self.latitude = %d, self.longitude = %d', self.latitude, self.longitude)
        from distance.models import Distance
        from Department.models import Department
        if self.latitude != 0 or self.longitude != 0:
            if create == False:
                distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE house_id_id = %s',[pk_val])
                for distance_item in distance_set:
                    distance_item.delete()
            department_set = Department.objects.raw('SELECT * FROM department_department WHERE latitude <> 0 and longitude <> 0')
            for department_item in department_set:
                gap = getSphereDistance(lat1=self.latitude, lon1=self.longitude, lat2=department_item.latitude, lon2=depratment_item.longitude)
                distance = Distance(house_id = department_item, department_id = self, distance = gap)
                distance.save()

    

