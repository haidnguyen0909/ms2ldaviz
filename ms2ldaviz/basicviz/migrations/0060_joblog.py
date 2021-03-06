# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 14:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicviz', '0059_auto_20170318_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(default=datetime.date.today)),
                ('tasktype', models.CharField(max_length=128, null=True)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Experiment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
