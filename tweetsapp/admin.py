from django.contrib import admin
from .models import SingleTweet 
from .forms import TweetModelForm
# Register your models here.



class TweetModelAdmin(admin.ModelAdmin):
	form = TweetModelForm


admin.site.register(SingleTweet, TweetModelAdmin)