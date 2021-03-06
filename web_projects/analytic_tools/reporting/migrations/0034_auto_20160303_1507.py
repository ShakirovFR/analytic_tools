# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0033_auto_20160303_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='salesRepresentative',
        ),
        migrations.AddField(
            model_name='product',
            name='PSA',
            field=models.ManyToManyField(to='reporting.PSA'),
        ),
        migrations.AddField(
            model_name='product',
            name='salesRepresentative',
            field=models.ManyToManyField(to='reporting.SalesRepresentative'),
        ),
        migrations.AddField(
            model_name='shipto',
            name='salesRepresentative',
            field=models.ManyToManyField(to='reporting.SalesRepresentative'),
        ),
        migrations.RemoveField(
            model_name='shipto',
            name='PSA',
        ),
        migrations.AddField(
            model_name='shipto',
            name='PSA',
            field=models.ManyToManyField(to='reporting.PSA'),
        ),
    ]
