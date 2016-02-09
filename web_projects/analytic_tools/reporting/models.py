from django.db import models

###################################################################################################

class Sap(models.Model):
	code	= models.IntegerField(unique = True)
	name	= models.CharField(max_length = 50)
	def __str__(self):
		return str(self.code)

class JD(models.Model):
	code	= models.IntegerField(unique = True)
	name	= models.CharField(max_length = 50)
	def __str__(self):
		return str(self.code)

class Unification(models.Model):
	code	= models.CharField(max_length = 15, unique = True)
	name	= models.CharField(max_length = 50, unique = True)
	sapCode	= models.ManyToManyField(Sap, blank = True)
	jdCode	= models.ManyToManyField(JD, blank = True)
	def __str__(self):
		return str(self.code)

class CVM(models.Model):
	code	= models.CharField(max_length = 5, unique = True)
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return str(self.name)

class Group(models.Model):
	code	= models.IntegerField(unique = True)
	def __str__(self):
		return str(self.code)

class SoldTo(models.Model):
	code	= models.ForeignKey(Unification, to_field = 'code')
	CVM		= models.ForeignKey(CVM, to_field = 'name', blank = True, null = True)
	group	= models.ForeignKey(Group, to_field = 'code', blank = True, null = True)
	def __str__(self):
		return str(self.code)

###################################################################################################

class PSA(models.Model):
	code	= models.CharField(max_length = 5, unique = True)
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return str(self.name)

class Country(models.Model):
	code	= models.CharField(max_length = 3, unique = True)
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return str(self.name)

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
	code	= models.ForeignKey(Unification, to_field = 'code')
	PSA		= models.ForeignKey(PSA, to_field = 'name', blank = True, null = True)
	region	= models.ForeignKey(Region, to_field = 'name', blank = True, null = True)
	def __str__(self):
		return str(self.code)

###################################################################################################

class Warehouse(models.Model):
	code	= models.CharField(max_length = 5, unique = True)
	name	= models.CharField(max_length = 3)
	def __str__(self):
		return str(self.code)

class ProductName(models.Model):
	name		= models.CharField(max_length = 30, unique = True)
	commonName	= models.CharField(max_length = 30)
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

class Product(models.Model):
	code			= models.IntegerField(unique = True)
	warehouseCode	= models.ForeignKey(Warehouse, to_field = 'code')
	name			= models.ForeignKey(ProductName, to_field = 'name')
	type			= models.ForeignKey(ProductType, to_field = 'name')
	subpackage		= models.ForeignKey(Subpackage, to_field = 'name')
	def __str__(self):
		return str(self.code)

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
	name			= models.CharField(max_length = 30, unique = True)
	deliveryForm	= models.ForeignKey(DeliveryForm, to_field = 'name')
	deliveryMethod	= models.ForeignKey(DeliveryMethod, to_field = 'name')
	def __str__(self):
		return str(self.name)

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

class Transaction(models.Model):
	date				= models.DateField()
	soldToCode			= models.ForeignKey(Unification, to_field = 'code', related_name = '+')
	shipToCode			= models.ForeignKey(Unification, to_field = 'code')
	productCode			= models.ForeignKey(Product, to_field = 'code')
	transportCode		= models.ForeignKey(Transport, to_field = 'code')
	salesRepresentative	= models.ForeignKey(SalesRepresentative, to_field = 'name')
	warehouseCode		= models.ForeignKey(Warehouse, to_field = 'code', related_name = '+')
	intercompanyCode	= models.ForeignKey(Warehouse, to_field = 'code', blank = True, null = True)
	shippedVolume		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	shippedAmount		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	def __str__(self):
		return str(self.date) + '-' + str(self.shipToCode) + '-' + str(self.productCode)

###################################################################################################

class Prediction(models.Model):
	date		= models.DateField()
	productCode	= models.ForeignKey(Product, to_field = 'code')
	budVolume	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	budNetSales	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	fcVolume	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	fcNetSales	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	estVolume	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	estNetSales	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	def __str__(self):
		return str(self.date)

###################################################################################################

class Delivery(models.Model):
	warehouseCode	= models.ForeignKey(Warehouse, to_field = 'code')
	shipToCode		= models.ForeignKey(Unification, to_field = 'code')
	transportCode	= models.ForeignKey(Transport, to_field = 'code')
	distance		= models.DecimalField(max_digits = 15, decimal_places = 0)
	def __str__(self):
		return str(self.warehouseCode) + '-' + str(self.shipToCode) + '-' + str(self.transportCode)

class EBITDA(models.Model):
	# warehouseProduction
	# warehoseDelivering
	# warehouseIntercompany
	# productCode
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
	# deliveryRoadDistance
	# deliveryRailDistance
	# salesOffice
	# salesRepresentative
	# shippedVolume
	# shippedAmount
	transaction					= models.OneToOneField(Transaction)
	tKmRoad						= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	tKmRail						= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	outboundFreightRoad			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	outboundFreightRail			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	packingMaterial				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	shippingStation				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	CMN							= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	productionTotal				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	productionVariable			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	productionFixed				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	productionIM				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	marketingAndSales			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	commercialMargin			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	administration				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	corporativeManufacturing	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	EBITDA						= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	netSalesPrice				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	outboundFreightRoad_t		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	outboundFreightRail_t		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	packingMaterial_t			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	shippingStation_t			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	CMN_t						= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	productionTotal_t			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	productionVariable_t		= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	productionFixed_t			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	productionIM_t				= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	marketingAndSales_t			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	commercialMargin_t			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	administration_t			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	corporativeManufacturing_t	= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	EBITDA_t					= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	EBITDA_percentage			= models.DecimalField(max_digits = 15, decimal_places = 2, blank = True, null = True)
	def __str__(self):
		return str(self.transaction)

###################################################################################################