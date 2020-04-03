from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import UserRegisterView
from .views import home 
from tweetsapp.views import TweetListView
from hashtags.views import HashTagView 
from .views import SearchView
from tweetsapp.api.views import SearchTweeAPIView
from hashtags.api.views import TagTweetAPIView
from django.contrib.auth import views as auth_views
from accounts.views import(
    loginPage,
    logoutPage,
    UserRegisterView,
    )





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^me/$', TweetListView.as_view(), name='me'),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
    url(r'^login/$', loginPage, name='login'),
    url(r'^logout/$', logoutPage, name='logout'),
    url(r'^search/$', SearchView.as_view(), name='search'),   
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^tweet/', include('tweetsapp.urls', namespace='tweet')),
    url(r'^api/tags/(?P<hashtag>.*)/$', TagTweetAPIView.as_view(), name='tag-tweet-api'),   
    url(r'^api/search/$', SearchTweeAPIView.as_view(), name='search-api'),
    url(r'^api/tweet/', include('tweetsapp.api.urls', namespace='tweet-api')),
    url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
    url(r'^', include('accounts.urls', namespace='profiles')),  


        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





#    