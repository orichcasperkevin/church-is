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
        fields = ('sender','message','type','time_stamp',)
        depth = 2
