# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jaf',
            name='profile',
        ),
        migrations.AddField(
            model_name='jaf',
            name='profile',
            field=models.ForeignKey(default='Analyst', on_delete=django.db.models.deletion.CASCADE, to='company.JobProfile', verbose_name='Job profile'),
        ),
    ]