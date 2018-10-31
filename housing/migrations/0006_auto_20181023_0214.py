# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0005_auto_20181023_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='location',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
