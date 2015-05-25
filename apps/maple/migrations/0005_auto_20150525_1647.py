# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0004_auto_20150525_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
