from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews,addviews

# TODO add delete views
urlpatterns = [
    # listing
    path('recent-news/', listviews.NewsList.as_view()),
    path('add-news/',addviews.AddNews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
