# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decomposition', '0015_auto_20170301_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='decomposition',
            name='status',
            field=models.CharField(choices=[(b'0', b'Pending'), (b'1', b'Ready')], default=b'1', max_length=128, null=True),
        ),
    ]
