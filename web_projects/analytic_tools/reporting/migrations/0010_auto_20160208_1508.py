# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0009_delete_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='JD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('jdCode', models.ManyToManyField(to='reporting.JD')),
                ('sapCode', models.ManyToManyField(to='reporting.Sap')),
            ],
        ),
        migrations.RemoveField(
            model_name='cementproductiontype',
            name='package',
        ),
        migrations.RemoveField(
            model_name='cementproductiontype',
            name='productName',
        ),
        migrations.RemoveField(
            model_name='cementproductiontype',
            name='productType',
        ),
        migrations.RemoveField(
            model_name='cementproductiontype',
            name='subPackage',
        ),
        migrations.RemoveField(
            model_name='cementproductiontype',
            name='warehouseName',
        ),
        migrations.RemoveField(
            model_name='customeraccount',
            name='segmentSoldTo',
        ),
        migrations.RemoveField(
            model_name='customershipto',
            name='segmentShipTo',
        ),
        migrations.RemoveField(
            model_name='region',
            name='area',
        ),
        migrations.RemoveField(
            model_name='region',
            name='country',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='cementProductionCode',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='accountName',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='cementProductionCode',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='intercompanyFrom',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='intercompanyTo',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='nameShipTo',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='regionName',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='salesRepresentative',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transportName',
        ),
        migrations.RemoveField(
            model_name='transporttype',
            name='transportHow',
        ),
        migrations.RemoveField(
            model_name='transporttype',
            name='transportWith',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='CementProductionType',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='CustomerAccount',
        ),
        migrations.DeleteModel(
            name='CustomerShipTo',
        ),
        migrations.DeleteModel(
            name='Package',
        ),
        migrations.DeleteModel(
            name='ProductName',
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
        migrations.DeleteModel(
            name='SalesRepresentative',
        ),
        migrations.DeleteModel(
            name='Segment',
        ),
        migrations.DeleteModel(
            name='SubPackage',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='TransportHow',
        ),
        migrations.DeleteModel(
            name='TransportType',
        ),
        migrations.DeleteModel(
            name='TransportWith',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
    ]
