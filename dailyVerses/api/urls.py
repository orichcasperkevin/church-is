from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews

# TODO add delete views
urlpatterns = [
    # listing
    path('verses-this-month/', listviews.VerseListThisMonth.as_view()),
    path('verse-today/', listviews.VerseToday.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
