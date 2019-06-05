from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews,addviews
#TODO add delete views
urlpatterns = [
   #listing
    path('income-type-list/', listviews.IncomeTypeList.as_view()),
    path('income-stats/', listviews.IncomeStats.as_view()),
    path('expenditure-type-list/', listviews.ExpenditureTypeList.as_view()),

    path('tithe-for-member/<int:id>/',listviews.TitheForMember.as_view()),
    path('tithe-stats-for-member/<int:id>/',listviews.TitheStatsForMember.as_view()),
    path('tithe-by-members-this-month/',listviews.TitheThisMonth.as_view()),
    path('tithe-stats/',listviews.TitheStats.as_view()),

    path('offerings-by-members-this-month/',listviews.OfferingThisMonth.as_view()),
    path('offering-stats-for-member/<int:id>/',listviews.OfferingStatsForMember.as_view()),
    path('offering-stats/',listviews.OfferingStats.as_view()),
    path('offerings-by-member/<int:id>/',listviews.OfferingByMember.as_view()),

    path('add-tithe-for-member/',addviews.addTithe.as_view()),
    path('add-offering/',addviews.addOffering.as_view()),
    path('add-group-offering/',addviews.addGroupOffering.as_view()),
    path('add-income/',addviews.addIncome.as_view()),
    path('add-expenditure/',addviews.addExpenditure.as_view())



]

urlpatterns = format_suffix_patterns(urlpatterns)
