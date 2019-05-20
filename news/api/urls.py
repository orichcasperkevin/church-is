from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews
#TODO add delete views
urlpatterns = [
   #listing
    path('news-today/', listviews.NewsListToday.as_view()),
    path('news-this-month/', listviews.NewsListThisMonth.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
