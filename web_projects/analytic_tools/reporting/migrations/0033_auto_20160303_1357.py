# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0032_remove_delivery_transportcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='shipToCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.ShipToFromDB', to_field='code'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='soldToCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.SoldToFromDB', to_field='code'),
        ),
    ]
