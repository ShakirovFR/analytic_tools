# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0017_auto_20160224_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='costCenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.CostCenter'),
        ),
    ]
