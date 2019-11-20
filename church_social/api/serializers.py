from rest_framework import serializers
from member.api.serializers import MemberSerializer
from church_social.models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

    def create(self, validated_data):
        name = validated_data.pop('name')
        tag = Tag.objects.get_or_create(name=name)
        return tag[0]

class DiscussionSerializer(serializers.ModelSerializer):
    creator = MemberSerializer()
    class Meta:
        model = Discussion
        fields = ('id','topic','creation_time','creator','open','tags',)
        depth = 2

class TagMembershipSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    discussion = DiscussionSerializer()
    class Meta:
        model = TagMembership
        depth = 1
        fields = ('discussion', 'tag',)

    def create(self, validated_data):
        tag= {}
        tag_data = validated_data.pop('tag')
        tag = Tag.objects.get(**tag_data)

        discussion = {}
        discussion_data = validated_data.pop('discussion')
        discussion = Discussion.objects.get(**discussion_data)

        tag_membership = TagMembership.objects.create(discussion=discussion,tag=tag)
        return tag_membership

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'description', 'open',)

class ChannelParticipantSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    class Meta:
        model = ChannelParticipant
        fields = ('channel',)
        depth = 1

class ChannelMessageSerializer(serializers.ModelSerializer):
    sender = MemberSerializer()
    class Meta:
        model = ChannelMessage
        fields = ('id','sender','message','type','time_stamp',)
        depth = 2

class PeerToPeerMessageSerializer(serializers.ModelSerializer):
    sender = MemberSerializer()
    receiver = MemberSerializer()
    class Meta:
        model = PeerToPeerMessage
        fields = ('id','chat_name','sender','receiver','message','time_stamp',)
