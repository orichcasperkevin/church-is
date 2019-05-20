from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from sermons.models import (Sermon,)

from sermons.api.serializers import (SermonSerializer,)

from datetime import date

today = date.today()
day = today.day
month = today.month
year = today.year

class SermonsToday(generics.ListCreateAPIView):
    '''
        get:
        sermons today
    '''
    queryset = Sermon.objects.filter(date__day = day)
    serializer_class = SermonSerializer

class SermonsThisMonth(generics.ListCreateAPIView):
    '''
        get:
        sermons this month
    '''
    queryset = Sermon.objects.filter(date__month = month)
    serializer_class = SermonSerializer
