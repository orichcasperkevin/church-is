from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews,detailviews,addviews
#TODO add delete views
urlpatterns = [
   #listing
    path('fellowship-list/', listviews.FellowshipList.as_view()),
    path('fellowship-meeting-list/<int:id>/',listviews.FellowshipMeetingList.as_view()),

    path('cell-group-list/', listviews.CellGroupList.as_view()),
    path('cell-group-meeting-list/<int:id>/',listviews.CellGroupMeetingList.as_view()),

    path('church-group-list/', listviews.ChurchGroupList.as_view()),
    path('church-group-meeting-list/<int:id>/',listviews.ChurchGroupMeetingList.as_view()),

    path('ministry-list/', listviews.MinistryList.as_view()),
    path('ministry-meeting-list/<int:id>/',listviews.MinistryMeetingList.as_view()),
   #detailviews
    path('fellowship/<int:id>/', detailviews.GetFellowshipWithId.as_view()),
    path('fellowship-members/<int:id>/', detailviews.GetMembersOfFellowshipWithId.as_view()),
    path('fellowship-members-match-pattern/<int:id>/<slug:pattern>/', detailviews.GetMembersOfFellowshipWithID_MatchPattern.as_view()),

    path('ministry/<int:id>/', detailviews.GetMinistryWithId.as_view()),
    path('ministry-members/<int:id>/', detailviews.GetMembersOfMinistryWithId.as_view()),

    path('church-group/<int:id>/', detailviews.GetChurchGroupWithId.as_view()),
    path('church-group-members/<int:id>/', detailviews.GetMembersOfChurchGroupWithId.as_view()),

    path('cell-group/<int:id>/', detailviews.GetCellGroupWithId.as_view()),
    path('cell-group-members/<int:id>/', detailviews.GetMembersOfCellGroupWithId.as_view()),


  #urls to add views
    path('add-member-to-group/', addviews.AddMemberToGroup.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
