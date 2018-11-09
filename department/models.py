from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=32,)
    location = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return str(self.id) + ' (' + self.name + ')'
