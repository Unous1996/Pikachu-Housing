# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_auto_20181111_1946'),
    ]

    '''
    operations = [
        migrations.AddField(
            model_name='department',
            name='latitude',
            field=models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)]),
        ),
        migrations.AddField(
            model_name='department',
            name='longitude',
            field=models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)]),
        ),
    ]
    '''