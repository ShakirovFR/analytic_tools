# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0019_auto_20160224_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionexpense',
            name='monthAndYear',
            field=models.CharField(max_length=7),
        ),
    ]
