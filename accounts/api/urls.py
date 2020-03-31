from django.conf.urls import url
from django.views.generic.base import RedirectView 
from tweetsapp.api.views import (
    SingleTweetListAPIView, 
     )


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/tweet/$', SingleTweetListAPIView.as_view(), name='list'),
]
