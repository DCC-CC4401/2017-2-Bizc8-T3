# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_auto_20171023_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateField(null=True),
        ),
    ]