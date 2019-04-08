from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews
#TODO add delete views 
urlpatterns = [
   #listing 
    path('fellowship-list/', listviews.FellowshipList.as_view()),
    path('fellowship-meeting-list/',listviews.FellowshipMeetingList.as_view()),
    path('cell-group-list/', listviews.CellGroupList.as_view()),
    path('cell-group-meeting-list/',listviews.CellGroupMeetingList.as_view()),
    path('church-group-list/', listviews.ChurchGroupList.as_view()),
    path('church-group-meeting-list/',listviews.ChurchGroupMeetingList.as_view()),
    path('ministry-list/', listviews.MinistryList.as_view()),
    path('ministry-meeting-list/',listviews.MinistryMeetingList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)