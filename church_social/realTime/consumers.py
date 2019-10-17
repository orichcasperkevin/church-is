# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from church_social.api.serializers import *
from member.models import Member

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'join_chat'
            }
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        channel = Channel.objects.get(name=self.room_name)
        sender = text_data_json['username']
        sender = Member.objects.get(member__username=sender)
        message = text_data_json['message']
        type = text_data_json['type']
        #record message to database
        message = ChannelMessage.objects.create(channel=channel,sender=sender,message=message,type=type)
        time_stamp = message.time_stamp
        time_stamp = str(time_stamp)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type': 'chat_message',
                'time_stamp': time_stamp
                }
        )
    # Receive message from room group
    def chat_message(self, event):
        # Send message to WebSocket
        time_stamp = event['time_stamp']
        message = ChannelMessage.objects.filter(time_stamp=time_stamp)        
        self.send(json.dumps(
            ChannelMessageSerializer(message, many=True).data)
            )

    def join_chat(self, event):
        print("someone joined chat")
