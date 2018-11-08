# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distance',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='distance',
            name='house_id',
        ),
        migrations.DeleteModel(
            name='Distance',
        ),
    ]
