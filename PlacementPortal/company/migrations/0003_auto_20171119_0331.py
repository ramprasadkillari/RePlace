# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20171118_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jaf',
            name='resume_number',
            field=models.IntegerField(choices=[(0, 'One page'), (1, 'Two page Tech'), (2, 'One page Nontech'), (3, 'CV')], default=0, verbose_name='Resume number'),
            preserve_default=False,
        ),
    ]
