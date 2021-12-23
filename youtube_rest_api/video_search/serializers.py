from rest_framework import serializers
from .models import Feed

class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = ('title','description','published_at','thumbnail_url','vid_id')
        