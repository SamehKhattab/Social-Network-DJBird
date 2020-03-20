from django.conf.urls import url
from django.views.generic.base import RedirectView 
from .views import (
    SingleTweetListAPIView, 
    SingleTweetCreateAPIView    )




urlpatterns = [
   
    url(r'^$', SingleTweetListAPIView.as_view(), name='list'),
    url(r'^create/$', SingleTweetCreateAPIView.as_view(), name='create'),
]

