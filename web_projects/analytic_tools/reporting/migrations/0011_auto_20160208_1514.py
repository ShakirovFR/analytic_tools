# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0010_auto_20160208_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jd',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='sap',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]