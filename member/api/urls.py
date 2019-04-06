from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews
#TODO add delete views 
urlpatterns = [
   #listing 
    path('member-list/', listviews.MemberList.as_view()),
    path('member-contact-list/', listviews.MemberContactList.as_view()),
    path('member-age-list/', listviews.MemberAgeList.as_view()),
    path('member-residence-list/', listviews.MemberResidenceList.as_view()),
    path('role-list/', listviews.RoleList.as_view()),
    path('member-role-list/', listviews.MemberRoleList.as_view()),
    path('member-marital-status-list/', listviews.MemberMaritalStatusList.as_view()),
    path('family-list/', listviews.FamilyList.as_view()),
    path('family-member-list/', listviews.FamilyMemberList.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)