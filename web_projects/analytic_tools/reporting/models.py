from django.db import models

###################################################################################################

class SoldToFromDB(models.Model):
    code	= models.IntegerField(unique = True)
    name	= models.CharField(max_length = 50)
    def __str__(self):
        return str(self.code)
  
class ShipToFromDB(models.Model):
    code	= models.IntegerField(unique = True)
    name	= models.CharField(max_length = 50)
    def __str__(self):
        return str(self.code)

###################################################################################################

class Office(models.Model):
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.name)

class SalesRepresentative(models.Model):
    office	= models.ForeignKey(Office, to_field = 'name')
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.name)

###################################################################################################

class CVM(models.Model):
    code	= models.CharField(max_length = 5, unique = True)
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.code)

class Group(models.Model):
    code	= models.IntegerField(unique = True)
    def __str__(self):
        return str(self.code)

class SoldTo(models.Model):
    code        = models.CharField(max_length = 15, unique = True)
    name        = models.CharField(max_length = 50, unique = True)
    codeFromDB  = models.ManyToManyField(SoldToFromDB)
    CVM         = models.ForeignKey(CVM, to_field = 'code', blank = True, null = True)
    group       = models.ForeignKey(Group, to_field = 'code', blank = True, null = True)
    def __str__(self):
        return str(self.code)

###################################################################################################

class PSA(models.Model):
    code	= models.CharField(max_length = 5, unique = True)
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.code)

class Country(models.Model):
    code	= models.CharField(max_length = 3, unique = True)
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.code)

class Area(models.Model):
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return str(self.name)

class Region(models.Model):
    country	= models.ForeignKey(Country, to_field = 'code')
    area	= models.ForeignKey(Area, to_field = 'name')
    code	= models.IntegerField()
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.name)

class ShipTo(models.Model):
    code                = models.CharField(max_length = 15, unique = True)
    name                = models.CharField(max_length = 50, unique = True)
    codeFromDB          = models.ManyToManyField(ShipToFromDB)
    region              = models.ForeignKey(Region, to_field = 'name', blank = True, null = True)
    PSA                 = models.ManyToManyField(PSA, blank = True)
    salesRepresentative = models.ManyToManyField(SalesRepresentative, blank = True)
    def __str__(self):
        return str(self.code)

###################################################################################################

class Warehouse(models.Model):
    code	= models.CharField(max_length = 5, unique = True)
    name	= models.CharField(max_length = 3)
    def __str__(self):
        return str(self.code)	

class ProductName(models.Model):
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.name)

class ProductType(models.Model):
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.name)

class Package(models.Model):
    name	= models.CharField(max_length = 15, unique = True)
    def __str__(self):
        return str(self.name)

class Subpackage(models.Model):
    package	= models.ForeignKey(Package, to_field = 'name')
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.name)

class ProductFromDB(models.Model):
    code	= models.IntegerField(unique = True)
    name	= models.CharField(max_length = 50)
    def __str__(self):
        return str(self.code)

class Product(models.Model):
    warehouseCode       = models.ForeignKey(Warehouse, to_field = 'code')
    name                = models.ForeignKey(ProductName, to_field = 'name')
    code                = models.ManyToManyField(ProductFromDB, blank = True)
    type                = models.ForeignKey(ProductType, to_field = 'name')
    subpackage          = models.ForeignKey(Subpackage, to_field = 'name')
    PSA                 = models.ManyToManyField(PSA)
    salesRepresentative = models.ManyToManyField(SalesRepresentative)
    def __str__(self):
        return str(self.warehouseCode) + '-' + str(self.name) + '-' + str(self.type) + '-' + str(self.subpackage)

###################################################################################################

class DeliveryForm(models.Model):
    name	= models.CharField(max_length = 15, unique = True)
    def __str__(self):
        return str(self.name)

class DeliveryMethod(models.Model):
    name	= models.CharField(max_length = 5, unique = True)
    def __str__(self):
        return str(self.name)

class Transport(models.Model):
    code			= models.CharField(max_length = 5, unique = True)
    name			= models.CharField(max_length = 30,  blank = True, null = True)
    deliveryForm	= models.ForeignKey(DeliveryForm, to_field = 'name')
    deliveryMethod	= models.ForeignKey(DeliveryMethod, to_field = 'name')
    def __str__(self):
        return str(self.code)

###################################################################################################

class Delivery(models.Model):
    warehouseCode	= models.ForeignKey(Warehouse, to_field = 'code')
    shipToCode		= models.ForeignKey(ShipTo, to_field = 'code')
    distance		= models.IntegerField()
    def __str__(self):
        return str(self.warehouseCode) + '-' + str(self.shipToCode)

###################################################################################################

class Transaction(models.Model):
    date				   = models.DateField()
    soldToCode			   = models.ForeignKey(SoldToFromDB, to_field = 'code', blank = True, null = True)
    shipToCode			   = models.ForeignKey(ShipToFromDB, to_field = 'code', blank = True, null = True)
    productCode		   = models.ForeignKey(ProductFromDB, to_field = 'code')
    transportCode		   = models.ForeignKey(Transport, to_field = 'code', blank = True, null = True)
    warehouseCode		   = models.ForeignKey(Warehouse, to_field = 'code', related_name = '+')
    intercompanyCode	   = models.ForeignKey(Warehouse, to_field = 'code', blank = True, null = True)
    shippedVolume		   = models.DecimalField(max_digits = 15, decimal_places = 2)
    shippedAmount		   = models.DecimalField(max_digits = 15, decimal_places = 2)
    def __str__(self):
        return str(self.date) + '-' + str(self.warehouseCode) + '-' + str(self.productCode)

###################################################################################################

class Prediction(models.Model):
    date		 = models.DateField()
    productName = models.ForeignKey(ProductName, to_field = 'name')
    budVolume	 = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    budNetSales = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    fcVolume	 = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    fcNetSales	 = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    estVolume	 = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    estNetSales = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    def __str__(self):
        return str(self.date) + '-' + str(self.productName)

###################################################################################################

class ProductionExpense(models.Model):
    monthAndYear	= models.CharField(max_length = 7)
    warehouseCode	= models.ForeignKey(Warehouse, to_field = 'code')
    productName	= models.ForeignKey(ProductName, to_field = 'name')
    variable		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    fixed			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    IM				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    def __str__(self):
        return str(self.monthAndYear) + '-' + str(self.warehouseCode) + '-' + str(self.productName)

class OtherExpense(models.Model):
    monthAndYear		= models.CharField(max_length = 7, unique = True)
    administration		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    marketingAndSales	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    def __str__(self):
        return str(self.monthAndYear)

###################################################################################################

class CostType(models.Model):
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.name)

class CostElement(models.Model):
    name	= models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return str(self.name)

class CostCenter(models.Model):
    name				= models.CharField(max_length = 9)
    warehouseCode		= models.ForeignKey(Warehouse, to_field = 'code')
    costType			= models.ForeignKey(CostType, to_field = 'name')
    productType		= models.ManyToManyField(ProductType, blank = True)
    deliveryMethod		= models.ManyToManyField(DeliveryMethod, blank = True)
    subpackage			= models.ManyToManyField(Subpackage, blank = True)
    costElement		= models.ForeignKey(CostElement, to_field = 'name')
    def __str__(self):
        return str(self.name)

class Distribution(models.Model):
    monthAndYear		= models.CharField(max_length = 7)
    costCenter			= models.ForeignKey(CostCenter)
    monthAmount		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    monthVolume		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    month_tKm			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    price				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    def __str__(self):
        return str(self.monthAndYear) + '-' + str(self.costCenter)

###################################################################################################

class EBITDA(models.Model):
    transaction                 = models.OneToOneField(Transaction)
    # warehouseProduction
    # warehoseDelivering
    # warehouseIntercompany
    # productName
    # productName
    # productType
    # productPackingType
    # productSubpackingType
    # soldToCode
    # soldToName
    # soldToCVM
    # soldToGroup
    # shipToCode
    # shipToName
    # shipToPSA
    # shipToCountry
    # shipToArea
    # shipToRegion
    # deliveryForm	
    # deliveryMethod
    deliveryRoadDistance		   = models.IntegerField(blank = True, null = True)
    deliveryRailDistance		   = models.IntegerField(blank = True, null = True)
    deliveryWaterDistance		   = models.IntegerField(blank = True, null = True)
    # salesOffice
    # salesRepresentative
    # shippedVolume
    # shippedAmount
    tKmRoad                     = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    tKmRail                     = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    tKmWater					   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    outboundFreightRoad		   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    outboundFreightRail		   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    outboundFreightWater		   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    packingMaterial			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    shippingStation			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    CMN							   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    productionTotal			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    productionVariable          = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    productionFixed			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    productionIM				   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    marketingAndSales			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    commercialMargin			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    administration				   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    corporativeManufacturing	   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    EBITDA						   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    netSalesPrice				   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    outboundFreightRoad_t		   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    outboundFreightRail_t		   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    outboundFreightWater_t	   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    packingMaterial_t			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    shippingStation_t			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    CMN_t						   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    productionTotal_t			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    productionVariable_t		   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    productionFixed_t			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    productionIM_t				   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    marketingAndSales_t		   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    commercialMargin_t			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    administration_t			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    corporativeManufacturing_t  = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    EBITDA_t					   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    EBITDA_percentage			   = models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
    def __str__(self):
        return str(self.transaction)

###################################################################################################