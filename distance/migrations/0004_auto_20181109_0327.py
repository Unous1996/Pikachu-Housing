# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distance', '0003_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distance',
            name='department_id',
            field=models.ForeignKey(related_name='depart_id', to='department.Department'),
        ),
        migrations.AlterField(
            model_name='distance',
            name='house_id',
            field=models.ForeignKey(related_name='house_id', to='housing.House'),
        ),
    ]
