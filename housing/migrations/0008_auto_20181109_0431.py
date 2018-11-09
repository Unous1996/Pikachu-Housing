# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0007_house_provider'),
    ]

    operations = [

        migrations.AddField(
            model_name='house',
            name='cover_img',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='house',
            name='imgs',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.CharField(max_length=128, blank=True), size=100),
        ),
    ]
