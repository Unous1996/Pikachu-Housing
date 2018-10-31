# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0004_auto_20181023_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='imgs_url',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
