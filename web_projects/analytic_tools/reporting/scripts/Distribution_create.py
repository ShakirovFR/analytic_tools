import os
import sys
import django

sys.path.append("/opt/web_projects/analytic_tools/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'analytic_tools.settings'
django.setup()

from reporting.models import CostCenter, Distribution
from Parsing_DistributionReport import valuesList, previousDate

print(previousDate.strftime('%m.%Y'))

costCenter = CostCenter.objects.all().order_by( "name" )

i = 0
for item in costCenter:
	try:
		Distribution.objects.get(monthAndYear	= previousDate.strftime('%m.%Y'),
								 costCenter		= CostCenter.objects.get( name = item.name, costElement = item.costElement))
		Distribution.objects.filter(monthAndYear	= previousDate.strftime('%m.%Y'),
									costCenter		= CostCenter.objects.get( name = item.name, costElement = item.costElement)).update(monthAmount = valuesList[i])
	except:
		Distribution.objects.create(monthAndYear	= previousDate.strftime('%m.%Y'),
									costCenter		= CostCenter.objects.get( name = item.name, costElement = item.costElement),
									monthAmount 	= valuesList[i])
	i += 1