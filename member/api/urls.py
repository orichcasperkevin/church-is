from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews,addviews,detailviews
#TODO add delete views
urlpatterns = [
   #listing
    path('member-list/', listviews.MemberList.as_view()),
    path('role-list/', listviews.RoleList.as_view()),
    path('filter-by-first_name/<slug:pattern>/',listviews.MemberWhereFirstNameLikePattern.as_view()),
    path('filter-by-gender/<slug:gender>/',listviews.MemberFilteredByGender.as_view()),
    path('filter-by-age/<int:min_age>/<int:max_age>/',listviews.MemberFilteredByAge.as_view()),
  #detail for a user
    path('member/<int:id>/', detailviews.GetMemberWithId.as_view()),
    path('contact-for-member/<int:id>/', detailviews.GetContactForMemberWithId.as_view()),
    path('age-for-member/<int:id>/', detailviews.GetAgeForMemberWithId.as_view()),
    path('residence-for-member/<int:id>/', detailviews.GetResidenceForMemberWithId.as_view()),
    path('roles-for-member/<int:id>/', detailviews.GetRoleForMemberWithId.as_view()),
    path('marital-status-for-member/<int:id>/', detailviews.GetMaritalStatusForMemberWithId.as_view()),
    path('family-for-member/<int:id>/', detailviews.GetFamilyForMemberWithId.as_view()),

    #adding
    path('add-member/', addviews.addMember.as_view()),
    path('add-member-contact/', addviews.AddMemberContact.as_view()),
    path('add-member-d_o_b/', addviews.AddMemberD_O_B.as_view()),
    path('add-member-residence/', addviews.AddMemberResidence.as_view()),
    path('add-member-marital-status/', addviews.AddMemberMaritalStatus.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)
