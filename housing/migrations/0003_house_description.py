# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_auto_20181021_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='description',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
