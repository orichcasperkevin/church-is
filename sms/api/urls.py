from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import addviews
#TODO add delete views
urlpatterns = [

    path('add-sms/',addviews.addSMS.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)
