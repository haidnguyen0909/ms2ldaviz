# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-20 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decomposition', '0007_auto_20170220_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentglobalmass2motif',
            name='overlap_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='documentglobalmass2motif',
            name='probability',
            field=models.FloatField(null=True),
        ),
    ]
