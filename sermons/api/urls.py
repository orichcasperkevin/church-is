from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews
#TODO add delete views
urlpatterns = [
   #listing
    path('sermons-today/', listviews.SermonsToday.as_view()),
    path('sermons-this-month/', listviews.SermonsThisMonth.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
