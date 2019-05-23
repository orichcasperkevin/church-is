from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from projects.models import (Project,Contribution,Pledge,PledgePayment)

from projects.api.serializers import (ProjectSerializer,ContributionSerializer,PledgeSerializer,PledgePaymentSerializer)

class ProjectList(generics.ListCreateAPIView):
    '''
        get:
        a list of Projects
        post:
        add a project
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectWithID(APIView):
    '''
        get project with id <id>
    '''
    def get(self,request,id):
        project = Project.objects.filter(id = id)
        data = ProjectSerializer(project,many=True).data
        return Response(data)

class ContributionsForAProject(APIView):
        '''
        contributions made by members for a project with id <id>
        '''
        def get(self,request,id):
            contribution = Contribution.objects.filter(project_id = id)
            data = ContributionSerializer(contribution,many=True).data
            return Response(data)

class ContributionsByAMember(APIView):
        '''
        contributions made by member with id <id>
        '''
        def get(self,request,id):
            contribution = Contribution.objects.filter(member__member_id = id)
            data = ContributionSerializer(contribution,many=True).data
            return Response(data)

class PledgesForAProject(APIView):
        '''
        pledges made by members for a project with id <id>
        '''
        def get(self,request,id):
            pledge = Pledge.objects.filter(project_id = id)
            data = PledgeSerializer(pledge,many=True).data
            return Response(data)

class PledgesByAmember(APIView):
        '''
        pledges made by member with id <id>
        '''
        def get(self,request,id):
            pledge = Pledge.objects.filter(member__member_id = id)
            data = PledgeSerializer(pledge,many=True).data
            return Response(data)

class PledgePaymentForAProject(APIView):
        '''
        pledges payment made by members for a project with id <id>
        '''
        def get(self,request,id):
            pledge_payment = PledgePayment.objects.filter(project_id = id)
            data = PledgePaymentSerializer(pledge_payment,many=True).data
            return Response(data)
class PledgePaymentForAMember(APIView):
        '''
        pledges payments made by member with id <id> for project with id <project_id>
        '''
        def get(self,request,id,project_id):
            pledge_payment = PledgePayment.objects.filter(pledge__project_id = project_id,pledge__member__member_id = id)
            data = PledgePaymentSerializer(pledge_payment,many=True).data
            return Response(data)