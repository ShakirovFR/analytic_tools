from django.contrib import admin
from reporting.models import *

def codeFromDB(obj):
    codeFromDB = obj.codeFromDB.values_list('code', flat = True)
    if len(codeFromDB) > 3:
        return str(codeFromDB[:3])[1:-1] + ', end more...'
    else:
        return str(codeFromDB)[1:-1]
    
codeFromDB.short_description = 'codeFromDB'

def getPSA(obj):
    PSA = str(obj.PSA.values_list('code', flat = True))[1:-1]
    if PSA == '':
        return '-'
    return PSA
getPSA.short_description = 'PSA'

def getSalesRepresentative(obj):
    getSalesRepresentative = str(obj.salesRepresentative.values_list('name', flat = True))[1:-1]
    if getSalesRepresentative == '':
        return '-'
    return getSalesRepresentative
getSalesRepresentative.short_description = 'salesRepresentative'

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal	= ('code', 'PSA', 'salesRepresentative')

class SoldToFromDBAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    
class ShipToFromDBAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    
class SoldToAdmin(admin.ModelAdmin):
    filter_horizontal	= ('codeFromDB',)
    list_display = ('code', 'name', codeFromDB, 'CVM', 'group')
    list_filter = ('CVM', 'group')
    search_fields = ('code', 'name')
 
class ShipToAdmin(admin.ModelAdmin):
    filter_horizontal	= ('codeFromDB', 'PSA', 'salesRepresentative')
    list_display = ('code', 'name', codeFromDB, getPSA, getSalesRepresentative)
    list_filter = ('PSA', 'salesRepresentative')
    search_fields = ('code', 'name')

admin.site.register(SoldToFromDB, SoldToFromDBAdmin)
admin.site.register(ShipToFromDB, ShipToFromDBAdmin)
admin.site.register(CVM)
admin.site.register(Group)
admin.site.register(SoldTo, SoldToAdmin)
admin.site.register(PSA)
admin.site.register(Country)
admin.site.register(Area)
admin.site.register(Region)
admin.site.register(ShipTo, ShipToAdmin)
admin.site.register(Warehouse)
admin.site.register(ProductName)
admin.site.register(ProductType)
admin.site.register(Package)
admin.site.register(Subpackage)
admin.site.register(ProductFromDB)
admin.site.register(Product, ProductAdmin)
admin.site.register(DeliveryForm)
admin.site.register(DeliveryMethod)
admin.site.register(Transport)
admin.site.register(Office)
admin.site.register(SalesRepresentative)
admin.site.register(Delivery)
admin.site.register(Transaction)
admin.site.register(Prediction)
admin.site.register(ProductionExpense)
admin.site.register(OtherExpense)
admin.site.register(CostType)
admin.site.register(CostElement)
admin.site.register(CostCenter)
admin.site.register(Distribution)
admin.site.register(EBITDA)