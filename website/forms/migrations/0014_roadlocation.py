# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0013_auto_20160629_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_id', models.IntegerField(max_length=10)),
                ('rlongitude', models.FloatField()),
                ('rlattitude', models.FloatField()),
            ],
        ),
    ]
