from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews,detailviews,addviews

# TODO add delete views
urlpatterns = [
    # listing
    path('service-types/', listviews.ServiceTypes.as_view()),
    path('services-this-month/', listviews.ServicesThisMonth.as_view()),
    path('services-today/', listviews.ServicesToday.as_view()),

    path('service-on-date/<slug:date>/of-type/<int:type_id>/', detailviews.ServiceOnDateOfType.as_view()),
    path('service-items-for-service/<int:service_id>/', detailviews.ServiceItemsForService.as_view()),

    path('add-service/', addviews.AddService.as_view()),
    path('add-service-item/', addviews.AddServiceItem.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
