# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0031_auto_20160302_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='transportCode',
        ),
    ]
