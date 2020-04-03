from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    UserDetailView,
    UserFollowView,
    UserProfileView,
    EditUserProfileView,
    )



urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
    url(r'^(?P<slug>[\w-]+)/profile/$', UserProfileView, name="userprofile"), 
    url(r'^(?P<slug>[\w-]+)/edit/$', EditUserProfileView, name="edituserprofile"), 


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)