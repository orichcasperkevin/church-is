from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChannelChatConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/notices/$', consumers.ChannelNoticeConsumer),
    re_path(r'ws/peer_to_peer_chat/(?P<room_name>.*)/$', consumers.PeerToPeerChatConsumer),
]
