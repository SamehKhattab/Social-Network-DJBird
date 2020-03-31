from django.conf.urls import url
from django.views.generic.base import RedirectView 
from .views import (
    SingleTweetListAPIView, 
    SingleTweetCreateAPIView,
    RetweetAPIView,
    LikeToggleAPIView, 
    SingleTweetDetailAPIView,
     )




urlpatterns = [
   
    url(r'^$', SingleTweetListAPIView.as_view(), name='list'),
    url(r'^create/$', SingleTweetCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', SingleTweetDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),    

]

