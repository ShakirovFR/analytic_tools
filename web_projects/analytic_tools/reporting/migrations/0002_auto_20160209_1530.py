# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipto',
            name='code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reporting.Unification'),
        ),
    ]
