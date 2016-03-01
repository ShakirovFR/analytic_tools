import os
import sys
import django

sys.path.append("/opt/web_projects/analytic_tools/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'analytic_tools.settings'
django.setup()

from reporting.models import Distribution

# distribution = Distribution.objects.first()
# print(distribution.monthAndYear,
	  # distribution.costCenter.name,
	  # distribution.costCenter.costType,
	  # distribution.costCenter.productType.all().values_list('name', flat = True),
	  # distribution.costCenter.deliveryMethod.all().values_list('name', flat = True),
	  # distribution.costCenter.subpackage.all().values_list('name', flat = True),
	  # distribution.costCenter.costElement,
	  # distribution.monthAmount,
	  # distribution.monthVolume,
	  # distribution.month_tKm,
	  # distribution.price)