import os
import sys
import django

sys.path.append("/opt/web_projects/analytic_tools/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'analytic_tools.settings'
django.setup()

from reporting.models import ProductionExpense, OtherExpense, Warehouse, ProductName
from Parsing_Expense import allData
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
previousDate = (today + relativedelta(months = -1))

for item in allData[0][2]:
	try:
		ProductionExpense.objects.get(monthAndYear	= previousDate.strftime('%m.%Y'),
									    warehouseCode	= Warehouse.objects.get(code = item[0]),
									    productName	= ProductName.objects.get(name = item[1]))
		ProductionExpense.objects.filter(monthAndYear	= previousDate.strftime('%m.%Y'),
                                        warehouseCode	= item[0],
    										productName	= item[1]).update(variable	= item[2],
    																		   fixed		= item[3],
																		       IM		    = item[4],)
	except:
		ProductionExpense.objects.create(monthAndYear	= previousDate.strftime('%m.%Y'),
										   warehouseCode	= Warehouse.objects.get(code = item[0]),
										   productName	    = ProductName.objects.get(name = item[1]),
										   variable		= item[2],
										   fixed			= item[3],
										   IM				= item[4],)

try:
	OtherExpense.objects.get(monthAndYear = previousDate.strftime('%m.%Y'))
	OtherExpense.objects.filter(monthAndYear = previousDate.strftime('%m.%Y')).update(administration	= allData[1][2][0][0],
																					  marketingAndSales	= allData[1][2][0][1])
except:
	OtherExpense.objects.create(monthAndYear		= previousDate.strftime('%m.%Y'),
                               administration		= allData[1][2][0][0],
    							  marketingAndSales	= allData[1][2][0][1])

print(len(allData[0][2]))