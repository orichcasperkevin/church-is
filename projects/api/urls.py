from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews, addviews, statviews

# TODO add delete views
urlpatterns = [
    # listing
    path('pending-confirmations/', listviews.PendingConfirmations.as_view()),
    path('project-list/', listviews.ProjectList.as_view()),
    path('project-with-id/<int:id>/', listviews.ProjectWithID.as_view()),

    path('contribution-for-project/<int:id>/', listviews.ContributionsForAProject.as_view()),
    path('contributions-by-member/<int:id>/', listviews.ContributionsByAMember.as_view()),

    path('pledges-for-project/<int:id>/', listviews.PledgesForAProject.as_view()),
    path('pledges-by-member/<int:id>/', listviews.PledgesByAmember.as_view()),

    path('pledge-payment-for-project/<int:id>/', listviews.PledgesForAProject.as_view()),
    path('pledge-payment-for-project/<int:project_id>/by-member/<int:id>/',listviews.PledgePaymentForAMember.as_view()),

    path('add-pending-confirmation/', addviews.AddPendingConfirmation.as_view()),
    path('add-contribution-to-project/', addviews.AddContribution.as_view()),
    path('add-non-member-contribution-to-project/', addviews.AddAnonymousContribution.as_view()),
    path('add-pledge-to-project/', addviews.AddPledge.as_view()),
    path('add-anonymous-pledge-to-project/', addviews.AddAnonymousPledge.as_view()),
    path('service-pledge/', addviews.AddPledgePayment.as_view()),

    path('confirm-payment/<int:pending_confirmation_id>/', listviews.ConfirmPayment.as_view()),

    #stats for projects
    path('project-general-stats/', statviews.ProjectFinancingStats.as_view()),
    path('project-size-stats/',statviews.ProjectSizeStats.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
