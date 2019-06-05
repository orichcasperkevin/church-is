from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from member.models import Member
from groups.models import ChurchGroup
from finance.models import (Offering,GroupOffering,Tithe,Income,IncomeType,
                                Expenditure,ExpenditureType,)

from groups.api.serializers import ChurchGroupSerializer
from member.api.serializers import MemberSerializer
from finance.api.serializers import (OfferingSerializer,GroupOfferingSerializer,addAnonymousOfferingSerializer,TitheSerializer,IncomeTypeSerializer,IncomeSerializer,
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
        serializer_to_use = 0
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
            serializer_to_use = 1

        recording_member_id = request.data.get("recording_member_id")
        queryset = Member.objects.filter(member_id = recording_member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        recording_member = serializer.data

        church_group_id = request.data.get("church_group_id")
        queryset = ChurchGroup.objects.filter(id = church_group_id)
        data = []
        for data in queryset:
            data = data
        serializer = ChurchGroupSerializer(data)
        church_group = serializer.data

        name_if_not_member = request.data.get("name_if_not_member")
        date = request.data.get("date")
        anonymous = request.data.get("anonymous")
        amount = request.data.get("amount")
        narration = request.data.get("narration")


        data = {'member':member,'amount':amount,'date':date,'anonymous':anonymous,'name_if_not_member':name_if_not_member,
                 'church_group':church_group,'recorded_by':recording_member}
        if (serializer_to_use == 0):
            serializer = OfferingSerializer(data=data)
        if (serializer_to_use == 1):
            serializer = addAnonymousOfferingSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#TODO fix the serializer
class addGroupOffering(APIView):
    '''
        add offering by a church group
    '''
    def post(self,request):
        recording_member_id = request.data.get("recording_member_id")
        recording_member = Member.objects.filter(member_id = recording_member_id)

        date = request.data.get("date")
        amount = request.data.get("amount")
        narration = request.data.get("narration")

        offering = Offering.objects.create(amount=amount,date=date,narration=narration)

        church_group_id = request.data.get("church_group_id")
        church_group = ChurchGroup.objects.get(id = church_group_id)

        GroupOffering.objects.create(offering=offering, church_group=church_group)
        obj = GroupOffering.objects.latest('id')
        queryset = {'qs':[obj]}
        data = []
        for data in queryset:
            data = data
        serializer = GroupOfferingSerializer(data)
        group_offering = serializer.data

        return Response(group_offering, status=status.HTTP_201_CREATED)
class addIncome(APIView):
    '''
        add an income of amount <amount> and type <id> with description
    '''
    def post(self,request):

        recording_member_id = request.data.get("recording_member_id")
        queryset = Member.objects.filter(member_id = recording_member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        recording_member = serializer.data

        income_type_id = request.data.get("income_type_id")
        queryset = IncomeType.objects.filter(id = income_type_id)
        data = []
        for data in queryset:
            data = data
        serializer = IncomeTypeSerializer(data)
        income_type = serializer.data

        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'recorded_by':recording_member,'type':income_type,'amount':amount,'narration':narration}
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
    def post(self,request):

        recording_member_id = request.data.get("recording_member_id")
        queryset = Member.objects.filter(member_id = recording_member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        recording_member = serializer.data

        expenditure_type_id = request.data.get("expenditure_type_id")
        queryset = ExpenditureType.objects.filter(id = expenditure_type_id)
        data = []
        for data in queryset:
            data = data
        serializer = ExpenditureTypeSerializer(data)
        expenditure_type = serializer.data

        amount = request.data.get("amount")
        narration = request.data.get("narration")

        data = {'recorded_by':recording_member,'type':expenditure_type,'amount':amount,'narration':narration}
        serializer = ExpenditureSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
