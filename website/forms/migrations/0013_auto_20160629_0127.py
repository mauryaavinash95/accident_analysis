# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0012_accidentidentification_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidentidentification',
            name='time',
            field=models.TimeField(default='00:00:00'),
        ),
    ]
