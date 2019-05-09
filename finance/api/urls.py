from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews
#TODO add delete views
urlpatterns = [
   #listing
    path('income-type-list/', listviews.IncomeTypeList.as_view()),
    path('expenditure-type-list/', listviews.ExpenditureTypeList.as_view()),
    path('tithe-for-member/<int:id>/',listviews.TitheForMember.as_view()),
    path('tithe-by-members-this-month/',listviews.TitheThisMonth.as_view()),

    path('offering-list/',listviews.OfferingThisMonth.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
