from datetime import date

from django.utils.timezone import now
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from member.api.serializers import *
from member.models import *


class MemberList(generics.ListCreateAPIView):
    '''
        get:
        return list of members
        post:
        create a new member
    '''
    queryset = Member.objects.all().order_by('-member__date_joined')
    serializer_class = MemberSerializer


class MemberWhereFirstNameLikePattern(APIView):
    '''
        get:
        returns a list of members whose first names contain the string pattern described in the slug parameter
    '''

    def get(self, request, pattern):
        result = Member.objects.filter(member__first_name__icontains=pattern)
        data = MemberSerializer(result, many=True).data
        return Response(data)


class MemberFilteredByGender(APIView):
    '''
        get:
        returns list of people filtered with gender
    '''

    def get(self, request, gender):
        if (gender == "M"):
            members = Member.objects.filter(gender=gender)
        if (gender == "F"):
            members = Member.objects.filter(gender=gender)
        if (gender == "null"):
            members = Member.objects.all()

        data = MemberSerializer(members, many=True).data
        return Response(data)


class MemberFilteredByAge(APIView):
    '''
        get:
        returns a list of members filtered by age
    '''

    def get(self, request, min_age, max_age):
        current = now().date()
        min_date = date(current.year - min_age, current.month, current.day)
        max_date = date(current.year - max_age, current.month, current.day)
        members = MemberAge.objects.filter(d_o_b__gte=max_date,
                                           d_o_b__lte=min_date)

        data = MemberAgeSerializer(members, many=True).data
        return Response(data)


class MemberContactList(generics.ListCreateAPIView):
    '''
        get:
        return list of member contacts
    '''
    queryset = MemberContact.objects.all()
    serializer_class = MemberContactSerializer


class MemberAgeList(generics.ListCreateAPIView):
    '''
        get:
        return list of member dates of birth
    '''
    queryset = MemberAge.objects.all()
    serializer_class = MemberAgeSerializer


class MemberResidenceList(generics.ListCreateAPIView):
    '''
        get:
        return list of member residences
    '''
    queryset = MemberResidence.objects.all()
    serializer_class = MemberResidenceSerializer


class RoleList(generics.ListCreateAPIView):
    '''
        get:
        return list of member roles
    '''
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class MemberMaritalStatusList(generics.ListCreateAPIView):
    '''
        get:
        return list of members and their marital status
    '''
    queryset = MemberMaritalStatus.objects.all()
    serializer_class = MemberMaritalStatusSerializer


class FamilyList(generics.ListCreateAPIView):
    '''
        get:
        return list of families
    '''
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


class FamilyMembershipList(generics.ListCreateAPIView):
    '''
        get:
        return list of family members
    '''
    queryset = FamilyMembership.objects.all()
    serializer_class = FamilyMembershipSerializer
