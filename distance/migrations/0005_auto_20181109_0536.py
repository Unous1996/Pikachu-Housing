# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distance', '0004_auto_20181109_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distance',
            name='department_id',
            field=models.ForeignKey(related_name='distance', to='department.Department'),
        ),
        migrations.AlterField(
            model_name='distance',
            name='house_id',
            field=models.ForeignKey(related_name='distance', to='housing.House'),
        ),
    ]
