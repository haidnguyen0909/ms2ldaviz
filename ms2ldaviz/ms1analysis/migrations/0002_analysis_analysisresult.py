# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0063_mass2motif_linkmotif'),
        ('ms1analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('group1', models.CharField(max_length=256)),
                ('group2', models.CharField(max_length=256)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='AnalysisResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pValue', models.FloatField(null=True)),
                ('foldChange', models.FloatField(null=True)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ms1analysis.Analysis')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Document')),
            ],
        ),
    ]
