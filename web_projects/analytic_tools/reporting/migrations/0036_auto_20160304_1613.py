# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-04 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0035_auto_20160304_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipto',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.Region', to_field='name'),
        ),
    ]
