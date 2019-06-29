from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews

# TODO add delete views
urlpatterns = [
    # listing
    path('event-list/', listviews.EventList.as_view()),
    path('expected-to-attend-event-list/<int:id>/', listviews.ExpectedToAttendEventList.as_view()),
    path('event-attendance-list/<int:id>/', listviews.EventAttendanceList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
