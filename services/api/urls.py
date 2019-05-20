from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews
#TODO add delete views
urlpatterns = [
   #listing
    path('services-this-month/', listviews.ServicesThisMonth.as_view()),
    path('services-today/', listviews.ServicesToday.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
