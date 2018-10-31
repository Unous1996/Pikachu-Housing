# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0003_house_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='description',
            field=models.CharField(max_length=600, blank=True),
        ),
    ]
