from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews,addviews

# TODO add delete views
urlpatterns = [
    # listing
    path('event-list/', listviews.EventsList.as_view()),

    #add
    path('add-event/', addviews.AddEvent.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
