from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews, addviews, updateviews, statviews, fileviews

# TODO add delete views
urlpatterns = [
    # listing
    path('pending-confirmations/', listviews.PendingConfirmations.as_view()),
    path('income-type-list/', listviews.IncomeTypeList.as_view()),
    path('income-type/<int:id>/', listviews.IncomeTypeOfID.as_view()),
    path('income-of-type/<int:id>/', listviews.IncomeOfType.as_view()),
    path('income-stats/', listviews.IncomeStats.as_view()),

    path('tithe-for-member/<int:id>/', listviews.TitheForMember.as_view()),
    path('tithe-stats-for-member/<int:id>/', listviews.TitheStatsForMember.as_view()),
    path('tithe-by-members-this-month/', listviews.TitheThisMonth.as_view()),
    path('tithe-stats/', listviews.TitheStats.as_view()),

    path('offering-types/', listviews.OfferingType.as_view()),
    path('offerings-by-members-this-month/', listviews.OfferingThisMonth.as_view()),
    path('offering-stats-for-member/<int:id>/', listviews.OfferingStatsForMember.as_view()),
    path('offering-stats/', listviews.OfferingStats.as_view()),
    path('offerings-by-member/<int:id>/', listviews.OfferingByMember.as_view()),

    path('expenditure-type-list/', listviews.ExpenditureTypeList.as_view()),
    path('expenditure-type/<int:id>/', listviews.ExpenditureTypeOfID.as_view()),
    path('expenditures-of-type/<int:id>/', listviews.ExpenditureOfType.as_view()),
    path('expenditure-stats/', listviews.ExpenditureStats.as_view()),

    path('add-tithe-for-member/', addviews.addTithe.as_view()),
    path('add-offering/', addviews.addOffering.as_view()),
    path('add-service-offering/', addviews.AddServiceOffering.as_view()),
    path('add-income/', addviews.addIncome.as_view()),
    path('add-expenditure/', addviews.addExpenditure.as_view()),
    path('add-pending-confirmation/', addviews.addPendingConfirmation.as_view()),

    path('confirm-payment/<int:pending_confirmation_id>/', updateviews.ConfirmPayment.as_view()),

    path('offering-by-member-stats/', statviews.OfferingFromMembers.as_view()),
    path('offering-by-type-stats/', statviews.OfferingByType.as_view()),
    path('offering-from-service-stats/', statviews.OfferingFromService.as_view()),
    path('tithe-general-stats/', statviews.TitheStats.as_view()),
    path('income-general-stats/', statviews.IncomeStats.as_view()),
    path('expenditure-general-stats/', statviews.ExpenditureStats.as_view()),

    #fileviews
    path('csv-test/',fileviews.some_view),
    path('get-tithes-as-csv/<slug:date>/',fileviews.get_tithes_csv),

]

urlpatterns = format_suffix_patterns(urlpatterns)
