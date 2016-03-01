# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import os
import time
from datetime import date
import sys
import django

sys.path.append("/opt/web_projects/analytic_tools/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'analytic_tools.settings'
django.setup()

from reporting.models import Transaction, ProductFromDB, Warehouse

def loading(fileName):
    path = ('/opt/files_store/Transactions/Input/%s.xlsx') % (fileName)
    wb = load_workbook(path, read_only = True)
    ws = wb.active
    return ws

def parsing(fileName, endDate, shift = 0):
    ws = loading(fileName)
    for row in ws['A1':'Z1048577']:
        date            = list(row)[shift + 2].value
        productCode     = list(row)[shift + 10].value
        warehouseCode   = list(row)[shift + 3].value
#       <--- replace master data --->
        if warehouseCode == 1:
            warehouseCode = 'U104'
        if warehouseCode == 5:
            warehouseCode = 'U103'
#       <--------------------------->
        shippedVolume   = list(row)[shift + 14].value
        shippedAmount   = list(row)[shift + 15].value
        intercompany = [14003280]
        try:
            if date.date() < endDate and int(productCode) not in intercompany :
                dataArray.append([date.date(),
                                  int(productCode),
                                  warehouseCode,
                                  shippedVolume,
                                  shippedAmount])
        except:
            pass

#<--- testing function --->
def unique(column):
    valTuple = []
    for item in dataArray:
        if item[column] not in valTuple:
            valTuple.append(item[column])
    return sorted(valTuple)
#<------------------------>

if __name__ == '__main__':
#   <--- rawinput --->
    year = 2016
    month = 2
    day = 26
#   <---------------->    
    clc = time.time()
    dataArray = []
    endDate = date(year, month, day)
    parsing('150914_Raw Data for Daily Report 2015', endDate)
    parsing('16.02.25', endDate, -1)
    Transaction.objects.filter(date__gte = date(year, month, 1)).delete()
    exceptions = []
    for item in dataArray:
        try:
            Transaction.objects.create(date          = item[0],
                                       productCode   = ProductFromDB.objects.get(code = item[1]),
                                       warehouseCode = Warehouse.objects.get(code = item[2]),
                                       shippedVolume = item[3],
                                       shippedAmount = item[4])
        except:
            if item[1] not in ProductFromDB.objects.all().values_list('code', flat = True) and item[1] not in exceptions:
                exceptions.append(item[1])
            if item[2] not in Warehouse.objects.all().values_list('code', flat = True) and item[2] not in exceptions:
                exceptions.append(item[2])
    for item in exceptions:
        print('Object %s not found' % item)
    print('Transactions count \t= %s' % len(dataArray))
    clc = time.time() - clc
    print('Script working time \t= {0:.2f} seconds'.format(clc))