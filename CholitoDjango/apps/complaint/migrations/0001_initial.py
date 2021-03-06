# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 04:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('complaintType', models.CharField(max_length=100)),
                ('place', models.CharField(default='santiago', max_length=100)),
                ('hurt', models.CharField(max_length=3)),
                ('sex', models.CharField(max_length=7)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('status', models.CharField(default='Reportada', max_length=100)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('commune', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
