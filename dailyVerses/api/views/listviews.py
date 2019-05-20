from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from dailyVerses.models import (Verse)
from dailyVerses.api.serializers import (VerseSerializer,)

from datetime import date

today = date.today()
day = today.day
month = today.month
year = today.year

class VerseToday(generics.ListCreateAPIView):
    '''
        get:
        the verse that's been created for this day
    '''
    queryset = Verse.objects.filter(day__day = day,day__month = month, day__year = year)
    serializer_class = VerseSerializer

class VerseListThisMonth(generics.ListCreateAPIView):
    '''
        get:
        a list of verses this month
    '''
    queryset = Verse.objects.filter(day__month = month, day__year = year)
    serializer_class = VerseSerializer
