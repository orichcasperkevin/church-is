from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import detailviews,addviews,updateviews

# TODO add delete views
urlpatterns = [
    # detailviews
    path('client/<int:id>/', detailviews.GetClient.as_view()),
    path('client-detail/<int:id>/', detailviews.GetClientDetail.as_view()),
    path('church-about/<int:id>/',detailviews.GetChurchAbout.as_view()),
    path('church-statements/<int:id>/',detailviews.GetChurchStatements.as_view()),
    path('church-core-values/<int:id>/',detailviews.GetChurchCoreValues.as_view()),
    path('church-periodic-themes/<int:id>/',detailviews.GetChurchPeriodicTheme.as_view()),

    #add
    path('add-church-mission-and-vision-statements/',addviews.AddChurchStatement.as_view()),
    path('add-church-about/',addviews.AddAboutChurch.as_view()),
    path('add-church-core-value/',addviews.AddChurchCoreValue.as_view()),
    path('add-theme/',addviews.AddChurchPeriodicTheme.as_view()),

    #update
    path('update-church-statements/',updateviews.UpdateChurchStatement.as_view()),
    path('update-about-church/',updateviews.UpdateAboutChurch.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
