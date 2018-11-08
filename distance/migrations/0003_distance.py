# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0007_house_provider'),
        ('department', '__first__'),
        ('distance', '0002_auto_20181107_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.FloatField(default=0)),
                ('department_id', models.ForeignKey(to='department.Department')),
                ('house_id', models.ForeignKey(to='housing.House')),
            ],
        ),
    ]
