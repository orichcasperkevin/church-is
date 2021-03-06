from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import listviews, addviews, detailviews, updateviews ,deleteviews,statviews

# TODO add delete views
urlpatterns = [
    #auth
    path('reset-password/', addviews.ResetPassword.as_view()),
    path('change-credentials/',addviews.ChangeUsernameAndPasswordView.as_view()),
    path('check-if-username-is-taken/',addviews.CheckIfUsernameIsTakenView.as_view()),
    path('get-permision-level/<int:id>/',detailviews.GetPermissionLevel.as_view()),

    # listing
    path('member-list/', listviews.MemberList.as_view()),
    path('role-list/', listviews.RoleList.as_view()),
    path('members-with-admin-roles/',listviews.GetMembersWithAdminRoles.as_view()),
    path('filter-by-first_name/<slug:pattern>/', listviews.MemberWhereFirstNameLikePattern.as_view()),
    path('filter-by-gender/<slug:gender>/', listviews.MemberFilteredByGender.as_view()),
    path('filter-by-age/<int:min_age>/<int:max_age>/<slug:gender>/', listviews.MemberFilteredByAge.as_view()),

    # detail for a user
    path('member/<int:id>/', detailviews.GetMemberWithId.as_view()),
    re_path(r'^member/(?P<username>.*)/$', detailviews.GetMemberWithUsername.as_view()),
    path('contact-for-member/<int:id>/', detailviews.GetContactForMemberWithId.as_view()),
    path('age-for-member/<int:id>/', detailviews.GetAgeForMemberWithId.as_view()),
    path('residence-for-member/<int:id>/', detailviews.GetResidenceForMemberWithId.as_view()),
    path('marital-status-for-member/<int:id>/', detailviews.GetMaritalStatusForMemberWithId.as_view()),
    path('family-for-member/<int:id>/', detailviews.GetFamilyForMemberWithId.as_view()),
    path('roles-for-member/<int:id>/', detailviews.GetRolesForMemberWithId.as_view()),

    # adding
    path('add-member/', addviews.addMember.as_view()),
    path('add-member-contact/', addviews.AddMemberContact.as_view()),
    path('add-member-d_o_b/', addviews.AddMemberD_O_B.as_view()),
    path('add-member-residence/', addviews.AddMemberResidence.as_view()),
    path('add-member-marital-status/', addviews.AddMemberMaritalStatus.as_view()),
    path('add-role-for-member/', addviews.AddRoleMemberShip.as_view()),
    path('upload-csv/', addviews.UploadCSV.as_view()),
    re_path(r'^preview-csv/(?P<file_name>.*)/$', detailviews.PreviewCSV.as_view()),
    path('check-csv/', addviews.CheckCSV.as_view()),
    path('import-data-from-csv/', addviews.ImportDataFromCsv.as_view()),

    #updating
    path('update-member-detail/',updateviews.UpdateMemberData.as_view()),
    path('update-member-residence/',updateviews.UpdateMemberResidence.as_view()),
    path('update-member-contact/',updateviews.UpdateMemberContact.as_view()),

    #BulkDeleteMember
    path('bulk-delete-members/',deleteviews.BulkDeleteMembers.as_view()),

    #statistics
    path('new-member-count/', statviews.NewMembersCount.as_view()),
    path('age-distribution/', statviews.AgeDistribution.as_view()),
    path('marital-status-distribution/', statviews.MaritalStatusDistribution.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)
