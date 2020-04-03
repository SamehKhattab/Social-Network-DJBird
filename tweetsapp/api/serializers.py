from rest_framework import serializers
from django.utils import timezone
import datetime
from tweetsapp.models import SingleTweet
from django.utils.timesince import timesince
from accounts.api.serializers import UserDisplaySerializer


class ParentTweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    unlikes = serializers.SerializerMethodField()
    did_unlike = serializers.SerializerMethodField()

    class Meta:
        model = SingleTweet
        fields = [
        'id',
        'user',
        'content',
        'timestamp',
        'date_display',
        'timesince', 
        'likes',
        'did_like',
        'unlikes',
        'did_unlike',
    
        ]


    def get_did_like(self, obj):
        request = self.context.get("request")
        try: 
            user = request.user
            if user.is_authenticated():
                if user in obj.liked.all():
                    return True
                elif user in obj.unliked.all():
                    return False
        except: 
            pass
        return False



    def get_likes(self, obj):
        return obj.liked.all().count() 


    def get_did_unlike(self, obj):
        request = self.context.get("request")
        try: 
            user = request.user
            if user.is_authenticated():
                if user in obj.unliked.all():
                    return True
                elif user in obj.liked.all():
                    return False
        except: 
            pass
        return False



    def get_unlikes(self, obj):
        return obj.unliked.all().count() 

    
    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y | %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + "  ago"




class SingleTweetModelSerializer(serializers.ModelSerializer):
    parent_id = serializers.CharField(write_only=True, required=False)
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    parent = ParentTweetModelSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    unlikes = serializers.SerializerMethodField()
    did_unlike = serializers.SerializerMethodField()
 

    class Meta:
        model = SingleTweet
        fields = [
        'parent_id',
        'id',
        'user',
        'content',
        'timestamp',
        'date_display',
        'timesince', 
        'parent', 
        'likes',
        'did_like',
        'unlikes',
        'did_unlike',
        'reply',

        ]


    def get_did_like(self, obj):
        request = self.context.get("request")
        try: 
            user = request.user
            if user.is_authenticated():
                if user in obj.liked.all():
                    return True
                elif user in obj.unliked.all():
                    return False
        except: 
            pass
        return False

    def get_likes(self, obj):
        return obj.liked.all().count() 


    def get_did_unlike(self, obj):
        request = self.context.get("request")
        try: 
            user = request.user
            if user.is_authenticated():
                if user in obj.unliked.all():
                    return True
                elif user in obj.liked.all():
                    return False
        except: 
            pass
        return False

    def get_unlikes(self, obj):
        return obj.unliked.all().count() 

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y | %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + "  ago"