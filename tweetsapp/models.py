import re
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse 
from django.utils import timezone
import datetime
from django.db.models.signals import post_save
from hashtags.signals import parsed_hashtags

# Create your models here.

class SingelTweetManager(models.Manager):
	def retweet(self, user, parent_obj):
		if parent_obj.parent:
			og_parent = parent_obj.parent
		else: 
			og_parent = parent_obj
			
		obj = self.model(
			parent = parent_obj,
			user = user, 
			content = parent_obj.content, 
			reply=False,
			)
		obj.save()
		return obj

	def like_toggle(self, user, tweet_obj):
		if user in tweet_obj.liked.all():
			is_liked = False
			tweet_obj.liked.remove(user)
		else: 
			is_liked = True
			tweet_obj.liked.add(user)
		return is_liked   

class SingleTweet(models.Model):
	parent 		= models.ForeignKey("self", blank=True, null=True)
	user		= models.ForeignKey(settings.AUTH_USER_MODEL)
	content 	= models.CharField(max_length=250)
	liked		= models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked')
	reply		= models.BooleanField(verbose_name='Is a reply?', default=False)
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects = SingelTweetManager()


	def __unicode__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})

	class Meta: 
		ordering = ['-timestamp']


	def get_parent(self):
		the_parent = self
		if self.parent:
			the_parent = self.parent
		return the_parent

	def get_children(self):
		parent = self.get_parent()
		qs = SingleTweet.objects.filter(parent = parent)
		qs_parent = SingleTweet.objects.filter(pk=parent.pk)
		return (qs | qs_parent)




def tweet_save_receiver(sender, instance, created, *args, **kwargs):
	if created and not instance.parent:
		user_regex = r'@(?P<username>[\w.@+-]+)'
		usernames = re.findall(user_regex, instance.content)

		hash_regex = r'#(?P<hashtag>[\w\d-]+)'
		hashtags = re.findall(hash_regex, instance.content)
		parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)

	post_save.connect(tweet_save_receiver, sender=SingleTweet)