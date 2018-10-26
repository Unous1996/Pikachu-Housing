# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '__first__'),
        ('housing', '0006_auto_20181023_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='provider',
            field=models.ForeignKey(blank=True, to='provider.Provider', null=True),
        ),
    ]
