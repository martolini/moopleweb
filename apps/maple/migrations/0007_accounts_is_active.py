# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0006_accounts_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
