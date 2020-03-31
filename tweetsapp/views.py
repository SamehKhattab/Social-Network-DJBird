from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.db.models import Q
from .models import SingleTweet
from .forms import TweetModelForm
from django.views.generic import View
from django.http import HttpResponseRedirect

# Create your views here.


class RetweetView(View):
	def get(self, request, pk, *args, **kwargs):
		tweet = get_object_or_404(SingleTweet, pk=pk)
		if request.user.is_authenticated():
			new_tweet = SingleTweet.objects.retweet(request.user, tweet)
			return HttpResponseRedirect("/")
		return HttpResponseRedirect(tweet.get_absolute_url())


class TweetDeleteView(DeleteView):
	model 			= SingleTweet
	template_name	='tweetsapp/delete_confirm.html'
	success_url		=reverse_lazy("tweet:list")


class TweetUpdateView(UpdateView):
	queryset 		= SingleTweet.objects.all()
	form_class 		= TweetModelForm
	template_name	='tweetsapp/update_view.html'


class TweetCreateView(CreateView):
	form_class 		= TweetModelForm
	template_name	='tweetsapp/create_view.html'
	
class TweetDetailView(DetailView):
	queryset = SingleTweet.objects.all()

class TweetListView(ListView):

	def get_queryset(self, *args, **kwargs):
		qs = SingleTweet.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query )|
				Q(user__username__icontains=query)
				)
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = TweetModelForm()
		context['create_url'] = reverse_lazy("tweet:create")
		return context








