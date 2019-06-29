from datetime import date

from rest_framework import generics

from services.api.serializers import (ServiceItemSerializer, )
# TODO import each componet singly
from services.models import (ServiceItem, )

today = date.today()
day = today.day
month = today.month
year = today.year


class ServicesToday(generics.ListCreateAPIView):
    '''
        a list of all services today
    '''
    queryset = ServiceItem.objects.filter(date__day=day, date__month=month, date__year=year)
    serializer_class = ServiceItemSerializer


class ServicesThisMonth(generics.ListCreateAPIView):
    '''
        a list of all services this month
    '''
    queryset = ServiceItem.objects.filter(date__month=month, date__year=year)
    serializer_class = ServiceItemSerializer
