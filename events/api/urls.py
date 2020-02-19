from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews,addviews,detailviews,statviews

# TODO add delete views
urlpatterns = [
    # listing
    path('event-list/', listviews.EventsList.as_view()),

    #detail
    path('events-by-group/<int:group_id>/',detailviews.GetEventsAttendedByGroup.as_view()),
    path('event/<int:event_id>/',detailviews.GetEvent.as_view()),
    path('event-where-pattern-like/<slug:pattern>/', detailviews.GetEventWhereTitleLikePattern.as_view()),
    path('get-groups-attending-event/<int:event_id>/',detailviews.GetGroupsAttendingEvent.as_view()),
    path('members-that-attended-event/<int:event_id>/', detailviews.GetMembersThatAttendedEvent.as_view()),

    #add
    path('add-event/', addviews.AddEvent.as_view()),
    path('add-group-attending-event/', addviews.AddGroupAttendingEvent.as_view()),
    path('record-member-that-attended-event/',addviews.RecordMemberThatAttendedEvent.as_view()),

    #stats
    path('event-count/',statviews.EventsCount.as_view()),
    path('event-attendance/', statviews.EventAttendance.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
