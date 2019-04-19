
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from groups.models import (Fellowship,CellGroup,ChurchGroup,Ministry)
from member.models import (Member,Role)

from groups.api.serializers import (FellowshipSerializer,AddMemberToFellowshipSerializer,
                                    CellGroupSerializer,AddMemberToCellGroupSerializer,
                                    ChurchGroupSerializer,AddMemberToChurchGroupSerializer,
                                    MinistrySerializer,AddMemberToMinistrySerializer)
from member.api.serializers import (RoleSerializer,MemberSerializer)

class AddMemberToGroup(APIView):
    '''

    '''
    def post(self,request):
        group_type = request.data.get("group_type")
        group_id = request.data.get("group_id")
        member_id = request.data.get("member_id")
        role_id = request.data.get("role_id")

        if (group_type == 'fellowship'):
            queryset = Fellowship.objects.filter(id = group_id)
            group = []
            for group in queryset:
                group = group
            serializer = FellowshipSerializer(group)
            fellowship = serializer.data

            queryset = Member.objects.filter(id = member_id)
            member = []
            for member in queryset:
                member = member
            serializer = MemberSerializer(member)
            member = serializer.data

            queryset = Role.objects.filter(id = role_id)
            role = []
            for role in queryset:
                role = role
            serializer = RoleSerializer(role)
            role = serializer.data

            data = {'fellowship':fellowship,'member':member,'role':role}
            serializer = AddMemberToFellowshipSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if (group_type == 'cell_group'):
            queryset = CellGroup.objects.filter(id = group_id)
            group = []
            for group in queryset:
                group = group
            serializer = CellGroupSerializer(group)
            cell_group = serializer.data

            queryset = Member.objects.filter(id = member_id)
            member = []
            for member in queryset:
                member = member
            serializer = MemberSerializer(member)
            member = serializer.data

            queryset = Role.objects.filter(id = role_id)
            role = []
            for role in queryset:
                role = role
            serializer = RoleSerializer(role)
            role = serializer.data

            data = {'cell_group':cell_group,'member':member,'role':role}
            serializer = AddMemberToCellGroupSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if (group_type == 'church_group'):
            queryset = ChurchGroup.objects.filter(id = group_id)
            group = []
            for group in queryset:
                group = group
            serializer = ChurchGroupSerializer(group)
            church_group = serializer.data

            queryset = Member.objects.filter(id = member_id)
            member = []
            for member in queryset:
                member = member
            serializer = MemberSerializer(member)
            member = serializer.data

            queryset = Role.objects.filter(id = role_id)
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

        if (group_type == 'ministry'):
            queryset = Ministry.objects.filter(id = group_id)
            group = []
            for group in queryset:
                group = group
            serializer = MinistrySerializer(group)
            ministry = serializer.data

            queryset = Member.objects.filter(id = member_id)
            member = []
            for member in queryset:
                member = member
            serializer = MemberSerializer(member)
            member = serializer.data

            queryset = Role.objects.filter(id = role_id)
            role = []
            for role in queryset:
                role = role
            serializer = RoleSerializer(role)
            role = serializer.data

            data = {'ministry':ministry,'member':member,'role':role}
            serializer = AddMemberToMinistrySerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
