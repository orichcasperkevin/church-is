from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from member.models import (Member,MemberContact,MemberAge,
                            MemberResidence,MemberRole,Role,
                            MemberMaritalStatus,Family,FamilyMember,)

from member.api.serializers import (MemberSerializer,MemberContactSerializer,MemberAgeSerializer,
                                    MemberResidenceSerializer,MemberRoleSerializer,
                                    RoleSerializer,MemberMaritalStatusSerializer,
                                    FamilySerializer,FamilyMemberSerializer,)

class MemberList(generics.ListCreateAPIView):
    '''
        get:
        return list of members
        post:
        create a new member
    '''
    queryset = Member.objects.all()
    serializer_class = MemberSerializer     

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

class MemberRoleList(generics.ListCreateAPIView):
    '''
        get:
        return list of members and their roles
    '''
    queryset = MemberRole.objects.all()
    serializer_class = MemberRoleSerializer

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

class FamilyMemberList(generics.ListCreateAPIView):
    '''
        get:
        return list of family members
    '''
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer