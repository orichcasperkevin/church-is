from rest_framework import serializers
from member.api.serializers import MemberSerializer
from church_social.models import *

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
