
from django.db import models
# Create your models here.

MOUNT_CHOICES = (
	('HR','Horizontal Rack Mount'),
	('VR','Vertical Rack Mount (Zero U)'),
)


MANAGEMENT_CHOICES = (
	('MS', 'Monitored & Switched'),
	('MT', 'Metered (Integrated LED Display)'),
	('BS', 'Basic'),
)


VOLTAGE_CHOICES = (
	('100-136', '100-136V'),
 	('100-250', '100-250V'),
	('200-250', '200-250V'),
	('120208-3', '120/208V 3PH'),
	('208-3', '208V 3PH'),
	('400230-3', '400/230V 3PH'),
)


AMP_CHOICES = (
	('20A', '20A'),
	('30A', '30A'),
	('32A', '32A'),
	('35A', '35A'),
	('40A', '40A (2x20A)'),
	('60A', '60A (2x30A)'),
)


PLUG_CHOICES = (
	('MIP', 'Modular Input Plug'),
	('MID', 'Modular Input Plug (Dual Ipput)'),
	('52P', '5-20P Input Plug'),
	('52A', '5-20P Input Plug w/ATX'),
	('5DP', '5-20P Input Plug (Dual Input)'),
	('L52', 'L5-20P Input Plug'),
	('L53', 'L5-30P Input Plug'),
	('D52', 'L5-20P Input Plug (Dual Input)'),
	('L62', 'L6-20P Input Plug'),
	('L63', 'L6-30P Input Plug'),
	('L12', 'L15-20P Delta Input Plug'),
	('L13', 'L15-30P Delta Input Plug'),
	('L21', 'L21-20P Delta Input Plug'),
	('W21', 'L21-20P WYE Input Plug'),
	('L23', 'L21-30P Delta Input Plug'),
	('W23', 'L21-30P Wye Input Plug'),
	('32A', '32A International Input Plug'),
	('CS8', 'CS8365C Input Plug'),
)


CORD_CHOICES = (
	('8', '8 ft.'),
	('12', '12 ft.'),
)


OUTVOLTAGE_CHOICES = (
	('10-36V', '100-136V'),
	('10-25V', '100-250V'),
	('20-25V', '200-250V'),
	('120V', '120V'),
	('208V', '208V'),
	('230V', '230V'),
	('vari', 'Various'),
)


OUTLET_CHOICES = (
	('4C19', '(4) C19'),
	('4L620', '(4) L6-20R'),
	('4L630', '(4) L6-30R'),
	('8C13', '(8) C13'),
	('8520R', '(8) 5-20R'),
	('8C19', '(8) C19'),
	('10C13', '(10) C13 (6) C19'),
	('1013C', '(10)C13'),
	('10R20', '(10) 5-20R'),
	('15C13', '(15) C13'), 
	('16520R', '(16) 5-20R'),	
	('20R20', '(20) 5-20R'),
	('16C13', '(16) C13'),	
	('21C13', '(21) C13'),
	('vary', 'Various'),
	('NO', 'none'),
)


	
class Product(models.Model):
	part_number 	= models.IntegerField(max_length=11, blank=False, unique=True)
	slug 		= models.SlugField(unique=True)
	category 	= models.ForeignKey('Category')  
	mount		= models.CharField(max_length=2, choices=MOUNT_CHOICES)  
	management	= models.CharField(max_length=2, choices=MANAGEMENT_CHOICES) 
	input_voltage	= models.CharField(max_length=8, choices=VOLTAGE_CHOICES)
	total_amprating = models.CharField(max_length=3, choices=AMP_CHOICES)
	input_plug	= models.CharField(max_length=3, choices=PLUG_CHOICES)
	cord_length 	= models.CharField(max_length=3, choices=CORD_CHOICES)
	output_voltage  = models.CharField(max_length=8, choices=OUTVOLTAGE_CHOICES)
	outlet		= models.CharField(max_length=10, choices=OUTLET_CHOICES)	
	base_price 	= models.CharField(max_length=6, blank=True) 
	description 	= models.TextField(blank=True) 

	#Product Picture Upload Fields
	front_pic 	= models.ImageField(upload_to="images/productpics/", blank=True) 
	side_pic 	= models.ImageField(upload_to="images/productpics/", blank=True) 
	plug_pic 	= models.ImageField(upload_to="images/productpics/", blank=True)
	outlet_pic 	= models.ImageField(upload_to="images/productpics/", blank=True)
	display_pic	= models.ImageField(upload_to="images/productpics/", blank=True)

	def __unicode__(self): 
		return self.slug 




class Category(models.Model): 
	name 		= models.CharField(max_length=200) 
	slug 		= models.SlugField(unique=True) 
	description 	= models.TextField(blank=True) 

	def __unicode__(self):
		return self.name
