from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from datetime import date

from member.models import (Member,MemberContact,MemberAge,
                            MemberResidence,MemberRole,Role,
                            MemberMaritalStatus,Family,FamilyMembership,)

from member.api.serializers import (UserSerializer,MemberSerializer,CreateMemberSerializer,MemberContactSerializer,MemberAgeSerializer,
                                    MemberResidenceSerializer,MemberRoleSerializer,
                                    RoleSerializer,MemberMaritalStatusSerializer,
                                    FamilySerializer,FamilyMembershipSerializer,)
class GetMemberWithId(APIView):
        '''
            get:
            get a member with id <id>
        '''
        def get(self,request,id):
            contact = Member.objects.filter(member__id = id)

            data = MemberSerializer(contact,many=True).data
            return Response(data)

class GetContactForMemberWithId(APIView):
        '''
            get:
            get a contact for a member with id <id>
        '''
        def get(self,request,id):
            contact = MemberContact.objects.filter(member__member__id = id)

            data = MemberContactSerializer(contact,many=True).data
            return Response(data)

class GetAgeForMemberWithId(APIView):
        '''
            get:
            get age for a member with id <id>
            and date of birth
        '''
        def get(self,request,id):
            age = MemberAge.objects.get(member__member__id = id)

            today = date.today()
            data = today.year - age.d_o_b.year - ((today.month, today.day) < (age.d_o_b.month, age.d_o_b.day))
            age_dict = { "age": '',"d_o_b": ''}
            age_dict["age"] = data
            age_dict["d_o_b"] = age.d_o_b

            data = age_dict

            return Response(data)

class GetResidenceForMemberWithId(APIView):
        '''
            get:
            get a residence for a member with id <id>
        '''
        def get(self,request,id):
            residence = MemberResidence.objects.filter(member__member__id = id)

            data = MemberResidenceSerializer(residence,many=True).data
            return Response(data)
class GetMaritalStatusForMemberWithId(APIView):
        '''
            get:
            get marital status for a member with id <id>
        '''
        def get(self,request,id):
            residence = MemberMaritalStatus.objects.filter(member__member__id = id)

            data = MemberMaritalStatusSerializer(residence,many=True).data
            return Response(data)
class GetRoleForMemberWithId(APIView):
        '''
            get:
            get roles for a member with id <id>
        '''
        def get(self,request,id):
            role = MemberRole.objects.filter(member__member__id = id)

            data = MemberRoleSerializer(role,many=True).data
            return Response(data)
class GetFamilyForMemberWithId(APIView):
        '''
            get:
            get the family members of the family the member belongs to
        '''
        def get(self,request,id):
            family_membership = FamilyMembership.objects.filter(member__member__id = id)

            data = FamilyMembershipSerializer(family_membership,many=True).data
            return Response(data)
