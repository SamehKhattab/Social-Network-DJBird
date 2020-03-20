from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home 
from tweetsapp.views import TweetListView


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='home'),
    url(r'^', include('accounts.urls', namespace='profiles')),
    url(r'^tweet/', include('tweetsapp.urls', namespace='tweet')),
  	url(r'^api/tweet/', include('tweetsapp.api.urls', namespace='tweet-api')),

]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))