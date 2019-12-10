from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.api.serializers import *
from projects.models import (Project, Contribution, Pledge, PledgePayment, PendingConfirmation)

class PendingConfirmations(generics.ListCreateAPIView):
    '''
        get:
        get the list of all pending confirmations
    '''
    queryset = PendingConfirmation.objects.all()
    serializer_class = PendingConfirmationSerializer

class ConfirmPayment(APIView):
    '''
        get:
        confirm a pending confirmation
    '''
    def get(self, request, pending_confirmation_id):
        data = {}
        pending_confirmation = PendingConfirmation.objects.get(id=pending_confirmation_id)
        confirmed = pending_confirmation.confirmPayment()
        if (pending_confirmation.type == "C"):
            data = ContributionSerializer(confirmed, many=True).data
        else:
            data = PledgePaymentSerializer(confirmed, many=True).data
        return Response(data)

class ProjectList(generics.ListCreateAPIView):
    '''
        get:
        a list of Projects
        post:
        add a project
    '''
    queryset = Project.objects.all().order_by('-start')
    serializer_class = ProjectSerializer


class ProjectWithID(APIView):
    '''
        get:
        get project with id <id>
    '''

    def get(self, request, id):
        project = Project.objects.filter(id=id)
        data = ProjectSerializer(project, many=True).data
        return Response(data)


class ContributionsForAProject(APIView):
    '''
        get:
        contributions made by members for a project with id <id>
    '''

    def get(self, request, id):
        contribution = Contribution.objects.filter(project_id=id).order_by('-recorded_at')
        data = ContributionSerializer(contribution, many=True).data
        return Response(data)


class ContributionsByAMember(APIView):
    '''
        get:
        contributions made by member with id <id>
    '''

    def get(self, request, id):
        contribution = Contribution.objects.filter(member__member_id=id).order_by('-recorded_at')
        data = ContributionSerializer(contribution, many=True).data
        return Response(data)


class PledgesForAProject(APIView):
    '''
        get:
        pledges made by members for a project with id <id>
    '''

    def get(self, request, id):
        pledge = Pledge.objects.filter(project_id=id)
        data = PledgeSerializer(pledge, many=True).data
        return Response(data)


class PledgesByAmember(APIView):
    '''
        get:
        pledges made by member with id <id>
    '''

    def get(self, request, id):
        pledge = Pledge.objects.filter(member__member_id=id)
        data = PledgeSerializer(pledge, many=True).data
        return Response(data)


class PledgePaymentForAProject(APIView):
    '''
        get:
        pledges payment made by members for a project with id <id>
    '''

    def get(self, request, id):
        pledge_payment = PledgePayment.objects.filter(project_id=id)
        data = PledgePaymentSerializer(pledge_payment, many=True).data
        return Response(data)


class PledgePaymentForAMember(APIView):
    '''
        get:
        pledges payments made by member with id <id> for project with id <project_id>
    '''

    def get(self, request, id, project_id):
        pledge_payment = PledgePayment.objects.filter(pledge__project_id=project_id, pledge__member__member_id=id)
        data = PledgePaymentSerializer(pledge_payment, many=True).data
        return Response(data)
