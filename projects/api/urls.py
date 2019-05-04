from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews
#TODO add delete views
urlpatterns = [
   #listing
    path('project-list/', listviews.ProjectList.as_view()),
    path('contribution-for-project/<int:id>/',listviews.ContributionsForAProject.as_view()),
    path('contribution-for-project/<int:project_id>/by-member/<int:id>/',listviews.ContributionsByAMember.as_view()),

    path('pledges-for-project/<int:id>/',listviews.PledgesForAProject.as_view()),
    path('pledges-for-project/<int:project_id>/by-member/<int:id>/',listviews.PledgesByAmember.as_view()),

    path('pledge-payment-for-project/<int:id>/',listviews.PledgesForAProject.as_view()),
    path('pledge-payment-for-project/<int:project_id>/by-member/<int:id>/',listviews.PledgePaymentForAMember.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
