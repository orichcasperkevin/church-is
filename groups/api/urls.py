from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews, detailviews, addviews, statviews,deleteviews

# TODO add delete views
urlpatterns = [
    # listing
    path('group-of-church-groups-list/', listviews.GroupOfChurchGroupsList.as_view()),
    path('church-group-list/', listviews.ChurchGroupList.as_view()),

    # detailviews
    path('church-groups-not-in-group/', detailviews.GetIndependentGroups.as_view()),
    path('church-groups-in-group/<int:id>/', detailviews.GetGroupsInGroupWithId.as_view()),
    path('church-group/<int:id>/', detailviews.GetChurchGroupWithId.as_view()),
    path('church-group-where-name-like/<slug:pattern>/',detailviews.GetGroupWhereNameLikePattern.as_view()),
    path('church-groups-for-a-member/<int:id>/', detailviews.GetChurchGroupsAMemberBelongsTo.as_view()),
    path('church-group-members/<int:id>/', detailviews.GetMembersOfChurchGroupWithId.as_view()),
    path('check-if-member/<int:member_id>/is-in-group/<int:group_id>/', detailviews.CheckIfMemberIsInGroup.as_view()),


    # urls to add views
    path('add-group/', addviews.AddGroup.as_view()),
    path('add-member-to-group/', addviews.AddMemberToGroup.as_view()),
    path('bulk-add-member-to-group/', addviews.BulkAddMembersToGroup.as_view()),

    #deleteself.
    path('remove-members-from-group/',deleteviews.RemoveMembersFromGroup.as_view()),

    #stats
    path("group-general-stats/", statviews.MemberCountStats.as_view()),
    path('group-attendance-stats/', statviews.EventAttendanceStats.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
