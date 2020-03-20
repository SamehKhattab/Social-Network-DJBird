from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse 
from django.utils import timezone
import datetime

# Create your models here.
class SingleTweet(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL)
	content 	= models.CharField(max_length=250)
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})

	class Meta: 
		ordering = ['-timestamp']
