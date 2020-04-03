from rest_framework import generics 
from tweetsapp.models import SingleTweet 
from .serializers import SingleTweetModelSerializer
from django.db.models import Q
from .serializers import SingleTweetModelSerializer
from rest_framework import permissions
from .pagination import StandardResultsPagination
from rest_framework.views import APIView 
from rest_framework.response import Response 


class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        tweet_qs = SingleTweet.objects.filter(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated():
            is_liked = SingleTweet.objects.like_toggle(request.user, tweet_qs.first())
            return Response({"liked": is_liked})
        
        return Response({"message": message}, status=400)


class UnLikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        tweet_qs = SingleTweet.objects.filter(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated():
            is_unliked = SingleTweet.objects.unlike_toggle(request.user, tweet_qs.first())
            return Response({"unliked": is_unliked})
        
        return Response({"message": message}, status=400)


class RetweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        tweet_qs = SingleTweet.objects.filter(pk=pk)
        message = "Not allowed"
        if tweet_qs.exists() and tweet_qs.count() == 1:
            #if request.user.is_authenticated():
            new_tweet = SingleTweet.objects.retweet(request.user, tweet_qs.first())
            if new_tweet is not None:
                data = SingleTweetModelSerializer(new_tweet).data
                return Response(data)
            message = "Error"
        return Response(None, status=400)


class SingleTweetCreateAPIView(generics.CreateAPIView):
    serializer_class = SingleTweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SingleTweetDetailAPIView(generics.ListAPIView):
    queryset = SingleTweet.objects.all()
    serializer_class = SingleTweetModelSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsPagination


    def get_queryset(self, *args, **kwargs):
        tweet_id = self.kwargs.get("pk")
        qs = SingleTweet.objects.filter(pk=tweet_id)
        if qs.exists() and qs.count() == 1:
            parent_obj = qs.first()
            qs1 = parent_obj.get_children()
            qs = (qs | qs1).distinct().extra(select={"parent_id_null": 'parent_id IS NULL'})
        return qs.order_by("-parent_id_null", '-timestamp')


class SingleTweetListAPIView(generics.ListAPIView):

    serializer_class = SingleTweetModelSerializer
    pagination_class = StandardResultsPagination
  
    
    def get_serializer_context(self, *args, **kwargs):
        context = super(SingleTweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context
        

    def get_queryset(self,*args, **kwargs):
        requested_user = self.kwargs.get("username")
       
        if requested_user:
            qs = SingleTweet.objects.filter(user__username=requested_user).order_by("-timestamp")
       
        else:
            im_following = self.request.user.profile.get_following()
            qs1 = SingleTweet.objects.filter(user__in=im_following)
            qs2 = SingleTweet.objects.filter(user=self.request.user)
            qs = (qs1 | qs2).distinct().order_by("-timestamp")
       
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
               Q(content__icontains=query) |
               Q(user__username__icontains=query)
                )

        return qs



class SearchTweeAPIView(generics.ListAPIView):

    queryset = SingleTweet.objects.all().order_by("-timestamp")
    serializer_class = SingleTweetModelSerializer
    pagination_class = StandardResultsPagination
  
    
    def get_serializer_context(self, *args, **kwargs):
        context = super(SearchTweeAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context
        
    def get_queryset(self,*args, **kwargs):
        qs = self.queryset       
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
               Q(content__icontains=query) |
               Q(user__username__icontains=query)
                )

        return qs
