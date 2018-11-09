# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0008_auto_20181109_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='imgs',
            field=django.contrib.postgres.fields.ArrayField(default=[], size=100, base_field=models.CharField(max_length=128, blank=True), blank=True),
        ),
    ]
