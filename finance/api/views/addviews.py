from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#import serializers
from finance.api.serializers import (OfferingSerializer, GroupOfferingSerializer,
    addAnonymousOfferingSerializer,TitheSerializer, IncomeTypeSerializer, IncomeSerializer,
    ExpenditureSerializer, ExpenditureTypeSerializer, AddServiceOfferingSerializer)

from member.api.serializers import MemberSerializer
from services.api.serializers import ServiceSerializer

# import models
from finance.models import (Offering, GroupOffering, IncomeType,ExpenditureType, )
from groups.models import ChurchGroup
from member.models import Member
from services.models import Service,ServiceType


class addTithe(APIView):
    '''
        add a tithe by a member.
    '''

    def post(self, request):

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
        narration = request.data.get("narration")

        data = {'member': member, 'amount': amount, 'narration': narration, 'recorded_by': recording_member}
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

    def post(self, request):
        serializer_to_use = 0
        member_id = request.data.get("member_id")
        if (member_id != None):
            queryset = Member.objects.filter(member_id=member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data
        else:
            member = None
            serializer_to_use = 1

        recording_member_id = request.data.get("recording_member_id")
        queryset = Member.objects.filter(member_id=recording_member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        recording_member = serializer.data

        name_if_not_member = request.data.get("name_if_not_member")
        date = request.data.get("date")
        anonymous = request.data.get("anonymous")
        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'member': member, 'amount': amount, 'date': date, 'anonymous': anonymous,
                'name_if_not_member': name_if_not_member,
                'recorded_by': recording_member}
        if (serializer_to_use == 0):
            serializer = OfferingSerializer(data=data)
        if (serializer_to_use == 1):
            serializer = addAnonymousOfferingSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddServiceOffering(APIView):
    '''
        add offering from a service
    '''

    def post(self, request):
        recording_member_id = request.data.get("recording_member_id")

        recording_member = Member.objects.filter(member_id=recording_member_id)
        queryset = Member.objects.filter(member_id=recording_member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        recording_member = serializer.data

        service_type_id = request.data.get("service_type_id")
        date = request.data.get("date")

        queryset = Service.objects.filter(type_id=service_type_id, date=date)
        data = []
        for data in queryset:
            data = data
            break
        serializer = ServiceSerializer(data)
        service = serializer.data

        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'service':service, 'date':date, 'amount': amount, 'narration': narration, 'recorded_by': recording_member}
        serializer = AddServiceOfferingSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class addIncome(APIView):
    '''
        add an income of amount <amount> and type <id> with description
    '''

    def post(self, request):

        recording_member_id = request.data.get("recording_member_id")
        queryset = Member.objects.filter(member_id=recording_member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        recording_member = serializer.data

        income_type_id = request.data.get("income_type_id")
        queryset = IncomeType.objects.filter(id=income_type_id)
        data = []
        for data in queryset:
            data = data
        serializer = IncomeTypeSerializer(data)
        income_type = serializer.data

        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'recorded_by': recording_member, 'type': income_type, 'amount': amount, 'narration': narration}
        serializer = IncomeSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addExpenditure(APIView):
    '''
        add an expenditure of amount <amount> and type <id> with description
    '''

    def post(self, request):

        recording_member_id = request.data.get("recording_member_id")
        queryset = Member.objects.filter(member_id=recording_member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        recording_member = serializer.data

        expenditure_type_id = request.data.get("expenditure_type_id")
        queryset = ExpenditureType.objects.filter(id=expenditure_type_id)
        data = []
        for data in queryset:
            data = data
        serializer = ExpenditureTypeSerializer(data)
        expenditure_type = serializer.data

        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'recorded_by': recording_member, 'type': expenditure_type, 'amount': amount, 'narration': narration}
        serializer = ExpenditureSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
