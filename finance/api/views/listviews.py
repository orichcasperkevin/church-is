from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from finance.models import (Offering,Tithe,Income,IncomeType,
                                Expenditure,ExpenditureType,)

from finance.api.serializers import (OfferingSerializer,TitheSerializer,IncomeTypeSerializer,IncomeSerializer,
                                        ExpenditureSerializer,ExpenditureTypeSerializer,)

from datetime import date

today = date.today()
day = today.day
month = today.month
year = today.year

class IncomeTypeList(generics.ListCreateAPIView):
    '''
        a list of all income types
    '''
    queryset = IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer


class ExpenditureTypeList(generics.ListCreateAPIView):
    '''
        a list of all expenditure types
    '''
    queryset = ExpenditureType.objects.all()
    serializer_class = ExpenditureTypeSerializer


class TitheForMember(APIView):
    '''
        tithes as given by member with id <id>
    '''
    def get(self,request,id):
        tithe  = Tithe.objects.filter(member__member_id = id)
        data = TitheSerializer(tithe,many=True).data
        return Response(data)

class TitheThisMonth(APIView):
    '''
        tithes as given by members this month
    '''
    def get(self,request):
        tithe = Tithe.objects.filter(date__month = month)
        data = TitheSerializer(tithe,many=True).data
        return Response(data)

class OfferingThisMonth(APIView):
    '''
        offerings this month
    '''
    def get(self,request):
        tithe = Offering.objects.filter(date__month = month)
        data = OfferingSerializer(tithe,many=True).data
        return Response(data)
