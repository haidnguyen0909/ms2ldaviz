# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0060_joblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotifMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(null=True)),
                ('frommotif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frommotif', to='basicviz.Mass2Motif')),
                ('tomotif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to='basicviz.Mass2Motif')),
            ],
        ),
    ]
