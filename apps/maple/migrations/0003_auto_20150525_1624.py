# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0002_auto_20150525_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='banned',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='characterslots',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='createdat',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='gender',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='gm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='greason',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='loggedin',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='tempban',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='tos',
            field=models.IntegerField(default=1),
        ),
    ]
