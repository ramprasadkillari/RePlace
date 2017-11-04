# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-04 11:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('type', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'Company ID')),
                ('name', models.CharField(max_length=50, verbose_name=b'Company name')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')], verbose_name=b'Phone number')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Category', verbose_name=b'Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JAF',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'JAF no.')),
                ('description', models.TextField(verbose_name=b'Job description')),
                ('other_details', models.TextField(blank=True, null=True, verbose_name=b'Other details')),
                ('requirements', models.TextField(verbose_name=b'Job requirements')),
                ('job_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1958), django.core.validators.MaxValueValidator(2018)], verbose_name=b'Registration year')),
                ('posting', models.CharField(max_length=50, verbose_name=b'Place of posting')),
                ('profile', models.CharField(max_length=50, verbose_name=b'Job profile')),
                ('accomodation', models.TextField(verbose_name=b'Accomodation details')),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(7)], verbose_name=b'Internship duration (days)')),
                ('resume_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name=b'Resume no. wanted')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name=b'Company')),
            ],
        ),
    ]