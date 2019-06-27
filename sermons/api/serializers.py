from rest_framework import serializers

from member.api.serializers import MemberSerializer
from member.models import Member
from sermons.models import (Sermon, )


class SermonSerializer(serializers.ModelSerializer):
    preached_by_member = MemberSerializer()

    class Meta:
        model = Sermon
        fields = ('title', 'slug', 'sermon', 'type', 'youtube_video_id',
                  'date', 'preached_by_member', 'preached_by', 'featured_image', 'website')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        preaching_member_data = validated_data.pop('preached_by_member')
        preaching_member = {}
        preaching_member = Member.objects.get(member_id=preaching_member_data["member"]["id"])

        sermon = Sermon.objects.create(preached_by_member=preaching_member, **validated_data)
        return sermon


class AddSermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = ('title', 'slug', 'sermon', 'type', 'youtube_video_id',
                  'date', 'preached_by', 'featured_image', 'website')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        sermon = Sermon.objects.create(**validated_data)
        return sermon
