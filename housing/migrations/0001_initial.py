# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('price', models.IntegerField(default=0)),
                ('imgs_url', models.CharField(max_length=64)),
                ('types', models.CharField(max_length=32)),
            ],
        ),
    ]
