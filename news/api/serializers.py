from rest_framework import serializers

from member.models import Member
from member.api.serializers import MemberSerializer
from news.models import (News,)

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('heading','slug','featured_image','church_group','fellowship','ministry','article',
                    'date','author','website')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
