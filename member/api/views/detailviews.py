from datetime import date

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from member.api.serializers import *
from member.models import *

from member.resources.importCSV import CSVLoader
loader = CSVLoader()

class GetMemberWithId(APIView):
    '''
        get:
        get a member with id <id>
    '''

    def get(self, request, id):
        member = Member.objects.filter(member__id=id)
        data = MemberSerializer(member, many=True).data
        return Response(data)

    def delete(self, request, id):
        member = Member.objects.get(member__id=id)
        member.delete()
        user = User.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetMemberWithUsername(APIView):
    '''
        get:
        get a member with username
    '''

    def get(self, request, username):
        member = Member.objects.filter(member__username=username)

        data = MemberSerializer(member, many=True).data
        return Response(data)


class GetContactForMemberWithId(APIView):
    '''
        get:
        get a contact for a member with id <id>
    '''

    def get(self, request, id):
        contact = MemberContact.objects.filter(member__member__id=id)

        data = MemberContactSerializer(contact, many=True).data
        return Response(data)


class GetAgeForMemberWithId(APIView):
    '''
        get:
        get age for a member with id <id>
        and date of birth
    '''

    def get(self, request, id):
        try:
            age = MemberAge.objects.get(member__member__id=id)
            today = date.today()
            data = today.year - age.d_o_b.year - ((today.month, today.day) < (age.d_o_b.month, age.d_o_b.day))
            age_dict = {"age": '', "d_o_b": ''}
            age_dict["age"] = data
            age_dict["d_o_b"] = age.d_o_b

            data = age_dict
            return Response(data)

        except:
            data = [None]
            return Response(data)



class GetResidenceForMemberWithId(APIView):
    '''
        get:
        get a residence for a member with id <id>
    '''

    def get(self, request, id):
        residence = MemberResidence.objects.filter(member__member__id=id)

        data = MemberResidenceSerializer(residence, many=True).data
        return Response(data)


class GetMaritalStatusForMemberWithId(APIView):
    '''
        get:
        get marital status for a member with id <id>
    '''

    def get(self, request, id):
        residence = MemberMaritalStatus.objects.filter(member__member__id=id)

        data = MemberMaritalStatusSerializer(residence, many=True).data
        return Response(data)


class GetFamilyForMemberWithId(APIView):
    '''
        get:
        get the family members of the family the member belongs to
    '''

    def get(self, request, id):
        family_membership = FamilyMembership.objects.filter(member__member__id=id)

        data = FamilyMembershipSerializer(family_membership, many=True).data
        return Response(data)


class GetRolesForMemberWithId(APIView):
    '''
        get:
        get the role groups the member belongs to
    '''

    def get(self, request, id):
        role_membership = RoleMembership.objects.filter(member__member__id=id)

        data = RoleMemberShipSerializer(role_membership, many=True).data
        return Response(data)

class PreviewCSV(APIView):
    '''
        get:
        get csv data for preview in the UI
    '''

    def get(self, request, file_name):
        loader.set_base_url(request.get_host())
        data = loader.preview_CSV(file_name)
        return Response(data)
