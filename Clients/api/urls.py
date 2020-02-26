from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import detailviews

# TODO add delete views
urlpatterns = [
    # detailviews
    path('client/<int:id>/', detailviews.GetClient.as_view()),
    path('client-detail/<int:id>/', detailviews.GetClientDetail.as_view()),
    path('church-statements/<int:id>/',detailviews.GetChurchStatements.as_view()),
    path('church-core-values/<int:id>/',detailviews.GetChurchCoreValues.as_view()),
    path('church-periodic-themes/<int:id>/',detailviews.GetChurchPeriodicTheme.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
