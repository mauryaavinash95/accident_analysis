# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 05:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0015_auto_20160705_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roadlocation',
            old_name='rlattitude',
            new_name='rlatitude',
        ),
    ]
