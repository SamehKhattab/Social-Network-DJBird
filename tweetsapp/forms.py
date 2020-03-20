from django import forms
from .models import SingleTweet

class TweetModelForm(forms.ModelForm):
	content = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':"What's up?!","class":"form-control"}))
	class Meta:
		model = SingleTweet
		fields = [
			"content",
		]
	