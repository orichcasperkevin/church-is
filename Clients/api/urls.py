from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import detailviews

# TODO add delete views
urlpatterns = [
    # detailviews
    path('client/<slug:formated_name_of_church>/', detailviews.GetClient.as_view()),
    path('client-detail/<slug:formated_name_of_church>/', detailviews.GetClientDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
