# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 19:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_remove_accidentidentification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidentidentification',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
