# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0013_auto_20181111_1948'),
    ]
    '''
    operations = [
        migrations.AddField(
            model_name='house',
            name='latitude',
            field=models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)]),
        ),
        migrations.AddField(
            model_name='house',
            name='longitude',
            field=models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)]),
        ),
    ]
    '''