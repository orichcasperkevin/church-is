from rest_framework.response import Response
from rest_framework.views import APIView
from church_social.api.serializers import *
from member.models import Member

class Channels(APIView):
    '''
        get:
        get channels a  member belongs
    '''
    def get(self, request, username):

        participant = ChannelParticipant.objects.filter(participant__member__username=username)
        data = ChannelParticipantSerializer(participant, many=True).data
        return Response(data)

class ChannelMessages(APIView):
    '''
        get:
        get channel messages
    '''
    def get(self,request,channel):
        message = ChannelMessage.objects.filter(channel__name=channel,type="M")
        data = ChannelMessageSerializer(message, many=True).data
        return Response(data)

class ChannelNotices(APIView):
    '''
        get:
        get channel public notices
    '''
    def get(self,request,channel):
        message = ChannelMessage.objects.filter(channel__name=channel,type="A").order_by('-time_stamp')
        data = ChannelMessageSerializer(message, many=True).data
        return Response(data)
