from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews, detailviews, addviews

# TODO add delete views
urlpatterns = [
    # listing
    path('group-of-church-groups-list/', listviews.GroupOfChurchGroupsList.as_view()),
    path('church-group-list/', listviews.ChurchGroupList.as_view()),
    path('church-group-meeting-list/<int:id>/', listviews.ChurchGroupMeetingList.as_view()),

    # detailviews
    path('church-groups-in-group/<int:id>/', detailviews.GetGroupsInGroupWithId.as_view()),
    path('church-group/<int:id>/', detailviews.GetChurchGroupWithId.as_view()),
    path('church-groups-for-a-member/<int:id>/', detailviews.GetChurchGroupsAMemberBelongsTo.as_view()),
    path('church-group-members/<int:id>/', detailviews.GetMembersOfChurchGroupWithId.as_view()),


    # urls to add views
    path('add-group/', addviews.AddGroup.as_view()),
    path('add-member-to-group/', addviews.AddMemberToGroup.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
