from rest_framework import serializers
from django.utils import timezone
import datetime
from tweetsapp.models import SingleTweet
from django.utils.timesince import timesince
from accounts.api.serializers import UserDisplaySerializer

class SingleTweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = SingleTweet
        fields = [
        'user',
        'content',
        'timestamp',
        'date_display',
        'timesince', 
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y | %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + "  ago"