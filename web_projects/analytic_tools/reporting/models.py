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
	sapCode	= models.ManyToManyField(Sap)
	jdCode	= models.ManyToManyField(JD)
	def __str__(self):
		return self.code

class CVM(models.Model):
	code	= models.CharField(max_length = 5, unique = True)
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return self.name

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
		return self.name

class Country(models.Model):
	code	= models.CharField(max_length = 3, unique = True)
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return self.name

class Area(models.Model):
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return self.name

class Region(models.Model):
	country	= models.ForeignKey(Country, to_field = 'code')
	area	= models.ForeignKey(Area, to_field = 'name')
	code	= models.IntegerField()
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return self.name

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
		return self.code

class ProductName(models.Model):
	name		= models.CharField(max_length = 30, unique = True)
	commonName	= models.CharField(max_length = 30)
	def __str__(self):
		return self.name

class ProductType(models.Model):
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return self.name

class Package(models.Model):
	name	= models.CharField(max_length = 15, unique = True)
	def __str__(self):
		return self.name

class Subpackage(models.Model):
	package	= models.ForeignKey(Package, to_field = 'name')
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return self.name

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
		return self.name

class DeliveryMethod(models.Model):
	name	= models.CharField(max_length = 5, unique = True)
	def __str__(self):
		return self.name

class Transport(models.Model):
	code			= models.CharField(max_length = 5, unique = True)
	name			= models.CharField(max_length = 30, unique = True)
	deliveryForm	= models.ForeignKey(DeliveryForm, to_field = 'name')
	deliveryMethod	= models.ForeignKey(DeliveryMethod, to_field = 'name')
	def __str__(self):
		return self.name

###################################################################################################

class Office(models.Model):
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return self.name

class SalesRepresentative(models.Model):
	office	= models.ForeignKey(Office, to_field = 'name')
	name	= models.CharField(max_length = 30, unique = True)
	def __str__(self):
		return self.name

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
		return str(self.date) + '-' + str(self.productCode)

###################################################################################################

class Delivery(models.Model):
	warehouseCode	= models.ForeignKey(Warehouse, to_field = 'code')
	shipToCode		= models.ForeignKey(Unification, to_field = 'code')
	transportCode	= models.ForeignKey(Transport, to_field = 'code')
	distance		= models.DecimalField(max_digits = 15, decimal_places = 0)
	def __str__(self):
		return self.warehouseCode + '-' + self.shipToCode + '-' + self.transportCode

class EBITDA(models.Model):
	# warehouseProduction		= models.ForeignKey(Warehouse, to_field = 'code', related_name = '+')
	# warehoseDelivering		= models.ForeignKey(Warehouse, to_field = 'code', related_name = '+')
	# warehouseIntercompany		= models.ForeignKey(Warehouse, to_field = 'code')
	# productCode				= models.ForeignKey(Product, to_field = 'code')
	# productName				= models.ForeignKey(Product, to_field = 'name')
	# productType				= models.ForeignKey(ProductType, to_field = 'name')
	# productPackingType		= models.ForeignKey(Package, to_field = 'name')
	# productSubpackingType		= models.ForeignKey(Subpackage, to_field = 'name')
	# soldToCode				= models.ForeignKey(Unification, to_field = 'code', related_name = '+')
	# soldToName				= models.ForeignKey(Unification, to_field = 'name', related_name = '+')
	# soldToCVM					= models.ForeignKey(CVM, to_field = 'name')
	# soldToGroup				= models.ForeignKey(Group, to_field = 'code')
	# shipToCode				= models.ForeignKey(Unification, to_field = 'code')
	# shipToName				= models.ForeignKey(Unification, to_field = 'name')
	# shipToPSA					= models.ForeignKey(PSA, to_field = 'name')
	# shipToCountry				= models.ForeignKey(Country, to_field = 'code')
	# shipToArea				= models.ForeignKey(Area, to_field = 'name')
	# shipToRegion				= models.ForeignKey(Region, to_field = 'name')
	# deliveryForm				= models.ForeignKey(DeliveryForm, to_field = 'name')	
	# deliveryMethod			= models.ForeignKey(DeliveryMethod, to_field = 'name')
	# deliveryRoadDistance		= models.ForeignKey(Delivery, to_field = 'distance', blank = True, null = True)
	# deliveryRailDistance		= models.ForeignKey(Delivery, to_field = 'distance', blank = True, null = True)
	# salesOffice				= models.ForeignKey(Office, to_field = 'name')
	# salesRepresentative		= models.ForeignKey(SalesRepresentative, to_field = 'name')
	# shippedVolume				= models.ForeignKey(Transaction, to_field = 'shippedVolume', blank = True, null = True)
	# shippedAmount				= models.ForeignKey(Transaction, to_field = 'shippedAmount', blank = True, null = True)
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

# class Warehouse(models.Model):
	# warehouseName	= models.CharField(unique = True, max_length = 10)
	# warehouseCode	= models.CharField(unique = True, max_length = 10)
	# def __str__(self):
		# return self.warehouseName

# class ProductName(models.Model):
	# productName	= models.CharField(unique = True, max_length = 50)
	# commonName	= models.CharField(max_length = 30)
	# def __str__(self):
		# return self.productName

# class Package(models.Model):
	# package	= models.CharField(unique = True, max_length = 15)
	# def __str__(self):
		# return self.package

# class SubPackage(models.Model):
	# subPackage	= models.CharField(unique = True, max_length = 20)
	# def __str__(self):
		# return self.subPackage

# class ProductType(models.Model):
	# productType	= models.CharField(unique = True, max_length = 20)
	# def __str__(self):
		# return self.productType

# class TransportWith(models.Model):
	# transportWith	= models.CharField(unique = True, max_length = 10)
	# def __str__(self):
		# return self.transportWith

# class TransportHow(models.Model):
	# transportHow	= models.CharField(unique = True, max_length = 10)
	# def __str__(self):
		# return self.transportHow

# class Segment(models.Model):
	# segment	= models.CharField(unique = True, max_length = 20)
	# def __str__(self):
		# return self.segment

# class Country(models.Model):
	# country	= models.CharField(unique = True, max_length = 3)
	# def __str__(self):
		# return self.country

# class Area(models.Model):
	# area	= models.CharField(unique = True, max_length = 15)
	# def __str__(self):
		# return self.area

# class CustomerAccount(models.Model):
	# accountName	= models.CharField(unique = True, max_length = 50)
	# accountNumber	= models.CharField(unique = True, max_length = 10)
	# segmentSoldTo	= models.ForeignKey(Segment, to_field = 'segment')
	# def __str__(self):
		# return self.accountName

# class CustomerShipTo(models.Model):
	# nameShipTo	= models.CharField(unique = True, max_length = 50)
	# numberShipTo	= models.CharField(unique = True, max_length = 10)
	# segmentShipTo	= models.ForeignKey(Segment, to_field = 'segment')
	# def __str__(self):
		# return self.nameShipTo
		
# class CementProductionType(models.Model):
	# cementProductionCode	= models.CharField(unique = True, max_length = 15)
	# warehouseName			= models.ForeignKey(Warehouse, to_field = 'warehouseName')
	# productName			= models.ForeignKey(ProductName, to_field = 'productName')
	# package				= models.ForeignKey(Package, to_field = 'package')
	# subPackage			= models.ForeignKey(SubPackage, to_field = 'subPackage')
	# productType			= models.ForeignKey(ProductType, to_field = 'productType')
	# def __str__(self):
		# return self.cementProductionCode
		
# class TransportType(models.Model):
	# transportName	= models.CharField(unique = True, max_length = 50)
	# transportCode	= models.CharField(unique = True, max_length = 5)
	# transportWith	= models.ForeignKey(TransportWith, to_field = 'transportWith')
	# transportHow	= models.ForeignKey(TransportHow, to_field = 'transportHow')
	# def __str__(self):
		# return self.transportName

# class Region(models.Model):
	# regionName		= models.CharField(unique = True, max_length = 30)
	# country			= models.ForeignKey(Country, to_field = 'country', default = 'RU')
	# area				= models.ForeignKey(Area, to_field = 'area')
	# regionCode		= models.CharField(max_length = 3)
	# regionDescription	= models.CharField(max_length = 50, blank = True, null = True)
	# def __str__(self):
		# return self.regionName

# class SalesRepresentative(models.Model):
	# salesRepresentative	= models.CharField(unique = True, max_length = 30)
	# def __str__(self):
		# return self.salesRepresentative

# class Transaction(models.Model):
	# accountName			= models.ForeignKey(CustomerAccount, to_field = 'accountName')
	# nameShipTo			= models.ForeignKey(CustomerShipTo, to_field = 'nameShipTo')
	# cementProductionCode	= models.ForeignKey(CementProductionType, to_field = 'cementProductionCode')
	# transportName			= models.ForeignKey(TransportType, to_field = 'transportName')
	# regionName			= models.ForeignKey(Region, to_field = 'regionName')
	# salesRepresentative	= models.ForeignKey(SalesRepresentative, to_field = 'salesRepresentative')
	# date					= models.DateField()
	# shippedVolume			= models.DecimalField(max_digits = 15, decimal_places = 2)
	# shippedAmount			= models.DecimalField(max_digits = 15, decimal_places = 2)
	# intercompanyFrom		= models.ForeignKey(Warehouse, to_field = 'warehouseName', blank = True, null = True, related_name = '+')
	# intercompanyTo		= models.ForeignKey(Warehouse, to_field = 'warehouseName', blank = True, null = True)
	# def __str__(self):
		# return self.date + self.accountName + self.cementProductionCode

# class Sales(models.Model):
	# cementProductionCode	= models.ForeignKey(CementProductionType, to_field = 'cementProductionCode')
	# date					= models.DateField()
	# budVolume				= models.DecimalField(max_digits = 15, decimal_places = 2)
	# budNetSales			= models.DecimalField(max_digits = 15, decimal_places = 2)
	# fcVolume				= models.DecimalField(max_digits = 15, decimal_places = 2)
	# fcNetSales			= models.DecimalField(max_digits = 15, decimal_places = 2)
	# estVolume				= models.DecimalField(max_digits = 15, decimal_places = 2)
	# estNetSales			= models.DecimalField(max_digits = 15, decimal_places = 2)
	# def __str__(self):
		# return self.date + self.cementProductionCode