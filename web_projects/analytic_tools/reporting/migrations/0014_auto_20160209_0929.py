# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0013_auto_20160209_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sap',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(),
        ),
    ]