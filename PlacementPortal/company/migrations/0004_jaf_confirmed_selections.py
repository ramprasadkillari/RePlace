# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20171119_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='jaf',
            name='confirmed_selections',
            field=models.BooleanField(default=False, verbose_name='Final Shortlisted?'),
        ),
    ]
