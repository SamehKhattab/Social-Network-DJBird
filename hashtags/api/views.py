from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions 
from rest_framework.views import APIView 
from rest_framework.response import Response
from tweetsapp.models import SingleTweet
from tweetsapp.api.pagination import StandardResultsPagination
from tweetsapp.api.serializers import SingleTweetModelSerializer
from hashtags.models import HashTag


class TagTweetAPIView(generics.ListAPIView):

    queryset = SingleTweet.objects.all().order_by("-timestamp")
    serializer_class = SingleTweetModelSerializer
    pagination_class = StandardResultsPagination
  
    
    def get_serializer_context(self, *args, **kwargs):
        context = super(TagTweetAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context
        
    def get_queryset(self,*args, **kwargs):
        hashtag = self.kwargs.get("hashtag")
        hashtag_obj = None
        try:
            hashtag_obj = HashTag.objects.get_or_create(tag=hashtag)[0]
        except:
            pass
        if hashtag_obj:
            qs = hashtag_obj.get_tweets()
            query = self.request.GET.get("q",None)
            if query is not None:
                qs = qs.filter(
                   Q(content__icontains=query) |
                   Q(user__username__icontains=query)
                    )

            return qs
        return None

