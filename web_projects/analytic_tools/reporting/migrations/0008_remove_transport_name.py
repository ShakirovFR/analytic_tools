# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0007_auto_20160209_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='name',
        ),
    ]
