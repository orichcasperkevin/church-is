from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#import serializers
from finance.api.serializers import *
from member.api.serializers import MemberSerializer
from services.api.serializers import ServiceSerializer
# import models
from finance.models import *
from groups.models import ChurchGroup
from member.models import Member
from services.models import Service,ServiceType

def getSerializerData(queryset,serializer_class):
    if len(queryset) == 0:
        return None
    data = queryset[0]
    return serializer_class(data).data


class addPendingConfirmation(APIView):
    '''
        add a pending confirmation
    '''

    def post(self, request):

        member_id = request.data.get("member_id")
        queryset = Member.objects.filter(member_id=member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        member = serializer.data

        amount = request.data.get("amount")
        type = request.data.get("type")
        confirmation_message = request.data.get("confirmation_message")

        data = {'confirming_for': member, 'amount': amount, 'confirmation_message': confirmation_message, 'type': type}
        serializer = PendingConfirmationSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class addTithe(APIView):
    '''
        add a tithe by a member.
    '''

    def post(self, request):
        data = request.data
        if data['member']:
            data['member'] = Member.objects.get(member_id=data['member']).id or None
        data['recorded_by'] = Member.objects.get(member_id=data['recorded_by']).id

        serializer = AddTitheSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addOffering(APIView):
    '''
        add a offering by a member.
    '''
    def post(self, request):
        data = request.data
        if data['member']:
            data['member'] = Member.objects.get(member_id=data['member']).id
        data['recorded_by'] = Member.objects.get(member_id=data['recorded_by']).id

        serializer = OfferingSerializer(data=data,partial=True)
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
        recording_member = getSerializerData(queryset,MemberSerializer)

        service_type_id = request.data.get("service_type_id")
        date = request.data.get("date")
        service = None
        service = Service.objects.filter(type_id=service_type_id, date=date).first()
        if service is not None:
            service = service.id

        type = request.data.get("offering_type")
        group = request.data.get("group")
        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'type':type, 'service':service, 'date':date,'group':group, 'amount': amount, 'narration': narration, 'recorded_by': recording_member}
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
        recording_member = getSerializerData(queryset,MemberSerializer)

        income_type_id = request.data.get("income_type_id")
        queryset = IncomeType.objects.filter(id=income_type_id)
        income_type = getSerializerData(queryset,IncomeTypeSerializer)

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
        recording_member = getSerializerData(queryset,MemberSerializer)

        expenditure_type_id = request.data.get("expenditure_type_id")
        queryset = ExpenditureType.objects.filter(id=expenditure_type_id)
        expenditure_type = getSerializerData(queryset,ExpenditureTypeSerializer)

        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'recorded_by': recording_member, 'type': expenditure_type, 'amount': amount, 'narration': narration}
        serializer = ExpenditureSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
