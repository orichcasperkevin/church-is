from datetime import date

from rest_framework import generics

from sermons.api.serializers import (SermonSerializer, )
# TODO import each componet singly
from sermons.models import (Sermon, )

today = date.today()
day = today.day
month = today.month
year = today.year


class SermonsToday(generics.ListCreateAPIView):
    '''
        get:
        sermons today
    '''
    queryset = Sermon.objects.filter(date__day=day)
    serializer_class = SermonSerializer


class SermonsThisMonth(generics.ListCreateAPIView):
    '''
        get:
        sermons this month
    '''
    queryset = Sermon.objects.filter(date__month=month)
    serializer_class = SermonSerializer
