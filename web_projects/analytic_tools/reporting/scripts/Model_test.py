# -*- coding: utf-8 -*-
import os
import sys
import django

sys.path.append("/opt/web_projects/analytic_tools/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'analytic_tools.settings'
django.setup()

from reporting.models import Product, ProductFromDB, ProductionExpense

print('<Наличие всех кодов продуктов в Product>')
productFromDB = ProductFromDB.objects.all()
codeList = []
product = Product.objects.all()
for item in product:
	for obj in item.code.all().values_list('code', flat = True):
		codeList.append(obj)
if productFromDB.count() - len(codeList) == 0:
	print('\tSuccess')
else:
	print('\tError')

def dublicates(modelName):
	itemList = []
	for item in modelName.objects.all():
		itemList.append(str(item))
	print('<Отсутствие дубликатов в %s>' % (modelName.__name__))
	success = True
	for item in itemList:
		if itemList.count(item) != 1:
			success = False
			print('\tError : ', item, '\n\tCount = ', itemList.count(item))
	if success == True:
		print('\tSuccess')

dublicates(Product)
dublicates(ProductionExpense)