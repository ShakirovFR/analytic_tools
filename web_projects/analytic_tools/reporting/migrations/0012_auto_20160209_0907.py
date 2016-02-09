# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0011_auto_20160208_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CVM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EBITDA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tKmRoad', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tKmRail', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('outboundFreightRoad', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('outboundFreightRail', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('packingMaterial', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('shippingStation', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('CMN', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('productionTotal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('productionVariable', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('productionFixed', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('productionIM', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('marketingAndSales', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('commercialMargin', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('administration', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('corporativeManufacturing', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('EBITDA', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('netSalesPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('outboundFreightRoad_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('outboundFreightRail_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('packingMaterial_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('shippingStation_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('CMN_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('productionTotal_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('productionVariable_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('productionFixed_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('productionIM_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('marketingAndSales_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('commercialMargin_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('administration_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('corporativeManufacturing_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('EBITDA_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('EBITDA_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('budVolume', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('budNetSales', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fcVolume', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fcNetSales', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('estVolume', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('estNetSales', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('commonName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PSA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Area', to_field='name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Country', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='SalesRepresentative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Office', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='ShipTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PSA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.PSA', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='SoldTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CVM', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.CVM', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='Subpackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Package', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shippedVolume', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('shippedAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('deliveryForm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.DeliveryForm', to_field='name')),
                ('deliveryMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.DeliveryMethod', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='unification',
            name='jdCode',
            field=models.ManyToManyField(blank=True, null=True, to='reporting.JD'),
        ),
        migrations.AlterField(
            model_name='unification',
            name='sapCode',
            field=models.ManyToManyField(blank=True, null=True, to='reporting.Sap'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='intercompanyCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.Warehouse', to_field='code'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='productCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Product', to_field='code'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='salesRepresentative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.SalesRepresentative', to_field='name'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='shipToCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Unification', to_field='code'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='soldToCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reporting.Unification', to_field='code'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transportCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Transport', to_field='code'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='warehouseCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reporting.Warehouse', to_field='code'),
        ),
        migrations.AddField(
            model_name='soldto',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Unification', to_field='code'),
        ),
        migrations.AddField(
            model_name='soldto',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.Group', to_field='code'),
        ),
        migrations.AddField(
            model_name='shipto',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Unification', to_field='code'),
        ),
        migrations.AddField(
            model_name='shipto',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.Region', to_field='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.ProductName', to_field='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='subpackage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Subpackage', to_field='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.ProductType', to_field='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='warehouseCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Warehouse', to_field='code'),
        ),
        migrations.AddField(
            model_name='prediction',
            name='productCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Product', to_field='code'),
        ),
        migrations.AddField(
            model_name='ebitda',
            name='transaction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reporting.Transaction'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='shipToCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Unification', to_field='code'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='transportCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Transport', to_field='code'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='warehouseCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Warehouse', to_field='code'),
        ),
    ]