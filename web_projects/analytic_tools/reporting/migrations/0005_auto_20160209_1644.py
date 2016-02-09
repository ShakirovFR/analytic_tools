# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_auto_20160209_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='distance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ebitda',
            name='deliveryRailDistance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ebitda',
            name='deliveryRoadDistance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ebitda',
            name='deliveryWaterDistance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
