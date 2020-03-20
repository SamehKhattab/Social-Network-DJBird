from rest_framework import generics 
from tweetsapp.models import SingleTweet 
from .serializers import SingleTweetModelSerializer
from django.db.models import Q
from .serializers import SingleTweetModelSerializer
from rest_framework import permissions
from .pagination import StandardResultsPagination

class SingleTweetCreateAPIView(generics.CreateAPIView):
    serializer_class = SingleTweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class SingleTweetListAPIView(generics.ListAPIView):

    serializer_class = SingleTweetModelSerializer
    pagination_class = StandardResultsPagination
    def get_queryset(self,*args, **kwargs):
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
