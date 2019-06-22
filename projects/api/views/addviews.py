from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from member.models import (Member,)
from projects.models import (Project,Pledge)
from projects.api.serializers import (ProjectSerializer,ContributionSerializer,PledgeSerializer,AddContributionSerializer,
                PledgePaymentSerializer,AddAnonymousContributionSerializer,AddAnonymousPledgeSerializer,AddPledgeSerializer)

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
            amount = request.data.get("amount")

            data = {'project':project,'member':member,'anonymous':anonymous,
                    'amount':amount,'recorded_by':recording_member}

            serializer = AddContributionSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AddAnonymousContribution(APIView):
    '''
        post:
        add an anonymous contribution to a project
    '''
    def post(self,request):

            project_id = request.data.get("project_id")
            queryset = Project.objects.filter(id=project_id)
            data = []
            for data in queryset:
                data = data
            serializer = ProjectSerializer(data)
            project = serializer.data

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

            data = {'project':project,'anonymous':anonymous,'names':names,
                        'phone':phone,'amount':amount,'recorded_by':recording_member}

            serializer = AddAnonymousContributionSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddPledge(APIView):
    '''
        post:
        add a pledge by a member to a project
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

            amount = request.data.get("amount")
            date = request.data.get("date")

            data = {'project':project,'member':member,'date':date,
                    'amount':amount,'recorded_by':recording_member}

            serializer = AddPledgeSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddAnonymousPledge(APIView):
    '''
        post:
        add a pledge by a non member to a project
    '''
    def post(self,request):
            project_id = request.data.get("project_id")
            queryset = Project.objects.filter(id=project_id)
            data = []
            for data in queryset:
                data = data
            serializer = ProjectSerializer(data)
            project = serializer.data

            recording_member_id = request.data.get("recording_member_id")
            queryset = Member.objects.filter(member_id=recording_member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            recording_member = serializer.data

            names = request.data.get("names")
            phone = request.data.get("phone")
            amount = request.data.get("amount")
            date = request.data.get("date")

            data = {'project':project,'date':date,'names':names,
                        'phone':phone,'amount':amount,'recorded_by':recording_member}

            serializer = AddAnonymousPledgeSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AddPledgePayment(APIView):
    '''
        post:
        add a pledge payment by a member to a project
    '''
    def post(self,request):

            pledge_id = request.data.get("pledge_id")

            queryset = Pledge.objects.filter(id = pledge_id)
            data = []
            for data in queryset:
                data = data
            serializer = PledgeSerializer(data)
            pledge = serializer.data

            recording_member_id = request.data.get("recording_member_id")
            queryset = Member.objects.filter(member_id=recording_member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            recording_member = serializer.data

            payment_amount = request.data.get("amount")


            data = {'pledge':pledge,'payment_amount':payment_amount,'payment_recorded_by':recording_member}

            serializer = PledgePaymentSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
