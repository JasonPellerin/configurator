from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


TITLE_CHOICES = (
	('MR', 'MR.'),
	('MRS', 'MRS.'),
	('MS', 'MS.'),
	('DR', 'DR.'),
)

TIME_CHOICES = (
	('1M', '1 Month'),
	('3M', '3 Months'),
	('6M', '6 Months'),
	('1Y', '1 Year'),
	('NS', 'Not Sure'),
)



class Customer(models.Model):
        user            = models.OneToOneField(User, related_name="profile")
        first_name      = models.CharField(max_length=100)
	last_name       = models.CharField(max_length=100)
        title           = models.CharField(max_length=3, choices=TITLE_CHOICES)
	Company_name	= models.CharField(max_length=200, blank=True)
	email		= models.EmailField()
	phone		= models.BigIntegerField(max_length=11)
	time_frame	= models.CharField(max_length=2, choices=TIME_CHOICES) 



        def __unicode__(self):
                return self.first_name


class UserProfile(models.Model):

        user            = models.OneToOneField(User, verbose_name=(u"user"), on_delete=models.CASCADE,)



        def __unicode__(self):
                return self.name
