# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='imgs_url',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='location',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='types',
            field=models.CharField(max_length=32, blank=True),
        ),
    ]
