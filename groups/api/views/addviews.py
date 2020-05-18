from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from groups.api.serializers import *
from groups.models import GroupOfChurchGroups, ChurchGroup, ChurchGroupMembership
from member.api.serializers import RoleSerializer, MemberSerializer
from member.models import Member, Role

from groups.api.serializers import  *
from member.api.serializers import RoleSerializer,MemberSerializer

def getSerializerData(queryset,serializer_class):
    data = queryset[0]
    return serializer_class(data).data

class AddGroup(APIView):
    '''
    post:
    add a group
    '''
    def post(self,request):
        serializer = ChurchGroupSerializer(data=request.data,partial=True)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddMemberToGroup(APIView):
    '''
        post:
        add a member to a group
    '''

    def post(self, request):
        data = request.data        
        data['member'] = Member.objects.get(member_id=data['member']).id
        if data['role'] == None:
            data['role'] = Role.objects.get_or_create(role='member')[0].id
        serializer = ChurchGroupMembershipSerializer(data=data,partial=True)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BulkAddMembersToGroup(APIView):
    '''
        post:
        add a member to a group
    '''

    def post(self, request):
        group_id = request.data.get("group_id")
        member_ids = request.data.get("member_ids")
        role_id = request.data.get("role_id")

        for id in member_ids:
            if ChurchGroupMembership.objects.filter(member__member_id=id,church_group_id=group_id).first():#if member
                pass
            else:
                try:
                    member  = Member.objects.get(member_id=id)
                    group = ChurchGroup.objects.get(id=group_id)
                    role = Role.objects.get_or_create(role="member")[0]
                    ChurchGroupMembership.objects.create(church_group=group,member = member,role=role)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_201_CREATED)
