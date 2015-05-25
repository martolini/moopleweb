# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0005_auto_20150525_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='is_staff',
            field=models.BooleanField(default=0),
        ),
    ]
