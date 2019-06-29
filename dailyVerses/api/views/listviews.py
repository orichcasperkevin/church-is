from datetime import date

from rest_framework import generics

from dailyVerses.api.serializers import (VerseSerializer, )
from dailyVerses.models import (Verse)

today = date.today()
day = today.day
month = today.month
year = today.year


class VerseToday(generics.ListCreateAPIView):
    '''
        get:
        the verse that's been created for this day
    '''
    queryset = Verse.objects.filter(day__day=day, day__month=month, day__year=year)
    serializer_class = VerseSerializer


class VerseListThisMonth(generics.ListCreateAPIView):
    '''
        get:
        a list of verses this month
    '''
    queryset = Verse.objects.filter(day__month=month, day__year=year)
    serializer_class = VerseSerializer
