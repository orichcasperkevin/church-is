from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from church_social.api.serializers import *
from member.models import Member

MAX_MESSAGE_COUNT = 200

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
        message = ChannelMessage.objects.filter(channel__name=channel,type="M").order_by('id')
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

class PeerChats(APIView):
    '''
        get:
        all chats by a peer specified by the <username>
    '''
    def get(self,request,username):
        criteria1 = Q(sender__member__username=username)
        criteria2 = Q(receiver__member__username=username)
        messages = PeerToPeerMessage.objects.filter(criteria1 | criteria2)\
                                            .order_by('chat_id').distinct('chat_id')

        data =  PeerToPeerMessageSerializer(messages,many=True).data
        return Response(data)

class PeerToPeerMessages(APIView):
    '''
        get:
        get peer to peer messages from a two peers starting from <last_seen_message_id> or
        get the last <MAX_MESSAGE_COUNT>
    '''
    def get(self, request,peer_1 ,peer_2):
        criteria1 =  Q(sender__member__username=peer_1,receiver__member__username=peer_2)
        criteria2 = Q(sender__member__username=peer_2,receiver__member__username=peer_1)

        messages = PeerToPeerMessage.objects.filter(criteria1 | criteria2).order_by('id')
        data =  PeerToPeerMessageSerializer(messages,many=True).data
        return Response(data)
