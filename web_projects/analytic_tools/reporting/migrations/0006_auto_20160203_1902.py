# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0005_auto_20160203_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='warehouseCode',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
