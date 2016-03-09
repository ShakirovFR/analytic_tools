# -*- coding: utf-8 -*-
import os
import sys
import django

sys.path.append("/opt/web_projects/analytic_tools/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'analytic_tools.settings'
django.setup()

from reporting.models import SoldToFromDB, ShipToFromDB, SoldTo, ShipTo 

def unificationSoldTo(targetFrom, targetTo):
    objFrom = SoldTo.objects.get(name = targetFrom)
    objTo = SoldTo.objects.get(name = targetTo)
    search = SoldToFromDB.objects.filter(name = targetFrom)
    for item in search:
        objTo.codeFromDB.add(SoldToFromDB.objects.get(code = item.code))
    objFrom.delete()
    
def unificationShipTo(targetFrom, targetTo):
    objFrom = ShipTo.objects.get(name = targetFrom)
    objTo = ShipTo.objects.get(name = targetTo)
    search = ShipToFromDB.objects.filter(name = targetFrom)
    for item in search:
        objTo.codeFromDB.add(ShipToFromDB.objects.get(code = item.code))
    objFrom.delete()

if __name__ == '__main__':
#    unificationSoldTo('', '')
#    unificationShipTo('', '')