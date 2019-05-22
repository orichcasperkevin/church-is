from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from services.models import (Service,ServiceItem,)

from services.api.serializers import (ServiceSerializer,ServiceItemSerializer,)

from datetime import date

today = date.today()
day = today.day
month = today.month
year = today.year

class ServicesToday(generics.ListCreateAPIView):
    '''
        a list of all services today
    '''
    queryset = ServiceItem.objects.filter(date__day = day,date__month = month, date__year = year)
    serializer_class = ServiceItemSerializer

class ServicesThisMonth(generics.ListCreateAPIView):
    '''
        a list of all services this month
    '''
    queryset = ServiceItem.objects.filter(date__month = month, date__year = year)
    serializer_class = ServiceItemSerializer
