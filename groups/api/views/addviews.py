from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from groups.api.serializers import GroupOfChurchGroupSerializer, ChurchGroupSerializer, AddMemberToChurchGroupSerializer
from groups.models import GroupOfChurchGroups, ChurchGroup
from member.api.serializers import RoleSerializer, MemberSerializer
from member.models import Member, Role

from groups.api.serializers import  AddChurchGroupSerializer, ChurchGroupSerializer,AddMemberToChurchGroupSerializer
from member.api.serializers import RoleSerializer,MemberSerializer
class AddGroup(APIView):
    '''
    post:
    add a group
    '''
    def post(self,request):
        group_of_groups_id = request.data.get("group_of_groups_id")
        name = request.data.get("name")
        description = request.data.get("description")

        serializer = None
        if (group_of_groups_id == None):
            data = {'name':name, 'description':description}
            serializer = ChurchGroupSerializer(data=data)
        else:
            queryset = GroupOfChurchGroups.objects.filter(id=group_of_groups_id)
            group = []
            for group in queryset:
                group = group
            serializer = GroupOfChurchGroupSerializer(group)
            group = serializer.data

            data = {'group':group, 'name':name, 'description':description}
            serializer = AddChurchGroupSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddMemberToGroup(APIView):
    '''
        post:
        add a member to a group
    '''

    def post(self, request):
        group_type = request.data.get("group_type")
        group_id = request.data.get("group_id")
        member_id = request.data.get("member_id")
        role_id = request.data.get("role_id")


        queryset = ChurchGroup.objects.filter(id=group_id)
        group = []
        for group in queryset:
            group = group
        serializer = ChurchGroupSerializer(group)
        church_group = serializer.data

        queryset = Member.objects.filter(id=member_id)
        member = []
        for member in queryset:
            member = member
        serializer = MemberSerializer(member)
        member = serializer.data

        queryset = Role.objects.filter(id=role_id)
        role = []
        for role in queryset:
            role = role
        serializer = RoleSerializer(role)
        role = serializer.data

        data = {'church_group':church_group,'member':member,'role':role}

        serializer = AddMemberToChurchGroupSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
