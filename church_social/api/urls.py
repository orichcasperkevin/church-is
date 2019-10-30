from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews

urlpatterns = [
    # listing
    path('<slug:username>/channels/', listviews.Channels.as_view()),
    path('<slug:channel>/messages/', listviews.ChannelMessages.as_view()),
    path('<slug:channel>/notices/', listviews.ChannelNotices.as_view()),
    path('<slug:username>/chats/', listviews.PeerChats.as_view()),
    path('<slug:peer_1>/<slug:peer_2>/chat-messages/', listviews.PeerToPeerMessages.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
