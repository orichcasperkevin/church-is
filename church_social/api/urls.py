from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews,addviews,updateviews

urlpatterns = [
    # listing
    path('<slug:username>/channels/', listviews.Channels.as_view()),
    path('<slug:channel>/messages/', listviews.ChannelMessages.as_view()),
    path('<slug:channel>/notices/', listviews.ChannelNotices.as_view()),
    path('discussions/<int:from_index>/<int:to_index>/', listviews.Discussions.as_view()),
    path('discussion/<int:discussion_id>/reactions/', listviews.DisccussionReactions.as_view()),
    path('member/<int:member_id>/reactions-to-discussion/<int:discussion_id>/', listviews.MemberHasReacted.as_view()),
    path('discussion/<int:discussion_id>/recomendations/', listviews.DisccussionRecomendations.as_view()),
    path('discussion/<int:discussion_id>/contributions/<int:from_index>/<int:to_index>/', listviews.ContributionsInDiscussion.as_view()),
    path('discussion/<int:discussion_id>/contributions-count/', listviews.ContributionsInDiscussionCount.as_view()),
    path('contribution/<int:contribution_id>/comments/<int:from_index>/<int:to_index>/', listviews.CommentsInContribution.as_view()),

    re_path(r'^(?P<username>.*)/chats/$', listviews.PeerChats.as_view()),
    re_path(r'^(?P<peer_1>.*)/(?P<peer_2>.*)/chat-messages/$', listviews.PeerToPeerMessages.as_view()),

    # adding
    path('add-tag/', addviews.AddTag.as_view()),
    path('add-discussion/', addviews.AddDiscussion.as_view()),
    path('add-tag-to-discussion/', addviews.AddTagToDiscussion.as_view()),
    path('add-reaction-to-discussion/', addviews.AddReactionToDiscussion.as_view()),
    path('add-contribution-to-discussion/', addviews.AddContributionToDiscussion.as_view()),
    path('add-comment-to-contribution/', addviews.AddCommentToContribution.as_view()),

    #updating
    path('vote-contribution/<int:contribution_id>/', updateviews.VoteContribution.as_view()),
    path('vote-comment/<int:comment_id>/', updateviews.VoteComment.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)
