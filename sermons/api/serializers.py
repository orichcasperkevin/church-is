from rest_framework import serializers

from member.models import Member
from member.api.serializers import MemberSerializer
from sermons.models import (Sermon,)

class SermonSerializer(serializers.ModelSerializer):
    preached_by_member = MemberSerializer()
    class Meta:
        model = Sermon
        fields = ('title','slug','sermon','type','youtube_video_id',
                    'date','preached_by_member','preached_by','featured_image','website')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
