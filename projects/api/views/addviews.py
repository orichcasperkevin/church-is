from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from member.models import (Member,)
from projects.models import (Project,)
from projects.api.serializers import (ProjectSerializer,ContributionSerializer)

from member.api.serializers import MemberSerializer

class AddContribution(APIView):
    '''
        post:
        add a contribution to a project
    '''
    def post(self,request):

            project_id = request.data.get("project_id")
            queryset = Project.objects.filter(id=project_id)
            data = []
            for data in queryset:
                data = data
            serializer = ProjectSerializer(data)
            project = serializer.data

            member_id = request.data.get("member_id")
            queryset = Member.objects.filter(member_id=member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data

            recording_member_id = request.data.get("recording_member_id")
            queryset = Member.objects.filter(member_id=recording_member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            recording_member = serializer.data

            anonymous = request.data.get("anonymous")
            names = request.data.get("names")
            phone = request.data.get("phone")
            amount = request.data.get("amount")

            data = {'project':project,'member':member,'anonymous':anonymous,'names':names,
                        'phone':phone,'amount':amount,'recorded_by':recording_member}

            serializer = ContributionSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
