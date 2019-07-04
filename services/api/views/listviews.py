from datetime import date

from rest_framework import generics

from services.api.serializers import (ServiceTypeSerializer ,ServiceItemSerializer, ServiceSerializer)
# TODO import each componet singly
from services.models import (ServiceType, ServiceItem, Service )

today = date.today()
day = today.day
month = today.month
year = today.year

class ServiceTypes(generics.ListCreateAPIView):
    '''
        a list of service types
    '''
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer

class ServicesToday(generics.ListCreateAPIView):
    '''
        a list of all services today
    '''
    queryset = Service.objects.filter(date__day=day, date__month=month, date__year=year)
    serializer_class = ServiceSerializer


class ServicesThisMonth(generics.ListCreateAPIView):
    '''
        a list of all services this month
    '''
    queryset = Service.objects.filter(date__month=month, date__year=year)
    serializer_class = ServiceSerializer
