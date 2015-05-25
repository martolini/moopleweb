# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0007_accounts_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
