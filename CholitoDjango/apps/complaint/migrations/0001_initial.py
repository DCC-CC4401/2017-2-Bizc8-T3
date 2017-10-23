# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 01:36
from __future__ import unicode_literals

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
                ('complaintype', models.CharField(max_length=100)),
                ('place', models.CharField(default=b'santiago', max_length=100)),
                ('hurt', models.CharField(max_length=3)),
                ('sex', models.CharField(max_length=7)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(default=b'reportada', max_length=100)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('commune', models.CharField(max_length=100)),
            ],
        ),
    ]
