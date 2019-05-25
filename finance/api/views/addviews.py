from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from member.models import Member
from groups.models import ChurchGroup
from finance.models import (Offering,Tithe,Income,IncomeType,
                                Expenditure,ExpenditureType,)

from groups.api.serializers import ChurchGroupSerializer
from member.api.serializers import MemberSerializer
from finance.api.serializers import (OfferingSerializer,TitheSerializer,IncomeTypeSerializer,IncomeSerializer,
                                        ExpenditureSerializer,ExpenditureTypeSerializer,)
class addTithe(APIView):
    '''
        add a tithe by a member.
    '''
    def post(self,request):

        member_id = request.data.get("member_id")
        queryset = Member.objects.filter(member_id = member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        member = serializer.data

        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'member':member,'amount':amount,'narration':narration}
        serializer = TitheSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class addOffering(APIView):
    '''
        add a tithe by a member.
    '''
    def post(self,request):

        member_id = request.data.get("member_id")
        if (member_id != None):
            queryset = Member.objects.filter(member_id = member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data
        else:
            member = None

        recording_member_id = request.data.get("recording_member_id")
        queryset = Member.objects.filter(member_id = recording_member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        recording_member = serializer.data

        church_group_id = request.data.get("church_group_id")
        if (church_group_id != None):
            queryset = ChurchGroup.objects.filter(id = church_group_id)
            data = []
            for data in queryset:
                data = data
            serializer = ChurchGroupSerializer(data)
            church_group = serializer.data
        else:
            church_group = {'church_group': None }

        name_if_not_member = request.data.get("name_if_not_member")
        date = request.data.get("date")
        anonymous = request.data.get("anonymous")
        amount = request.data.get("amount")
        narration = request.data.get("narration")


        data = {'member':member,'amount':amount,'date':date,'anonymous':anonymous,'name_if_not_member':name_if_not_member,
                 'church_group':church_group,'recorded_by':recording_member}
        serializer = OfferingSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
