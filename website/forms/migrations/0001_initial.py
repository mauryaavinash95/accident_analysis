# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccidentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=500)),
                ('road_name', models.CharField(max_length=500)),
                ('road_type', models.CharField(max_length=100)),
                ('road_number', models.CharField(max_length=100)),
                ('no_lanes', models.IntegerField()),
                ('physical_divider', models.BooleanField()),
                ('road_surface', models.CharField(max_length=50)),
                ('accident_spot', models.CharField(max_length=100)),
                ('road_chainage', models.CharField(max_length=100)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('property_damage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AccidentIdentification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('fir_no', models.CharField(max_length=30)),
                ('police_station', models.CharField(max_length=30)),
                ('date_time', models.DateTimeField()),
                ('area_type', models.CharField(max_length=30)),
                ('accident_type', models.CharField(max_length=30)),
                ('no_vehicles', models.IntegerField()),
                ('no_fatalities', models.IntegerField()),
                ('no_injured_hospitalisation', models.IntegerField()),
                ('no_injured_not_hospitalisation', models.IntegerField()),
                ('hit_run', models.BooleanField()),
                ('ongoing_road_work', models.BooleanField()),
                ('weather_type', models.CharField(max_length=30)),
                ('collision_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehiclesInvolved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('reg_no', models.CharField(max_length=100)),
                ('disposition', models.CharField(max_length=100)),
                ('load_condition', models.CharField(max_length=100)),
                ('traffic_violation', models.CharField(max_length=100)),
                ('mechanical_failure', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='VictimsInvolved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('vehicle_occupant', models.CharField(max_length=100)),
                ('license_no', models.CharField(max_length=100)),
                ('impacted_by', models.CharField(max_length=100)),
                ('injury_type', models.CharField(max_length=100)),
                ('using_safety_device', models.BooleanField()),
                ('alcohol_drug', models.BooleanField()),
            ],
        ),
    ]
