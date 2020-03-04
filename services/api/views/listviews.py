from datetime import date

from rest_framework import generics

from services.api.serializers import *

from services.models import ServiceType, ServiceItem, Service

today = date.today()
day = today.day
month = today.month
year = today.year

class ServiceTypes(generics.ListCreateAPIView):
    '''
        a list of service types
    '''
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeListSerializer

class ServicesToday(generics.ListCreateAPIView):
    '''
        a list of all services today
    '''
    queryset = ServiceItem.objects.filter(service__date__day=day, service__date__month=month, service__date__year=year)
    serializer_class = ServiceItemSerializer


class ServicesThisMonth(generics.ListCreateAPIView):
    '''
        a list of all services this month
    '''
    queryset = ServiceItem.objects.all().order_by('-service__date')[:20]
    serializer_class = ServiceItemSerializer
