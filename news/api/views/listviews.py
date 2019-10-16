from datetime import date

from rest_framework import generics

from news.api.serializers import (NewsSerializer, )
from news.models import (News, )

today = date.today()
day = today.day
month = today.month
year = today.year


class NewsListToday(generics.ListCreateAPIView):
    '''
        news today
    '''
    queryset = News.objects.filter(date__day=day, date__month=month, date__year=year)
    serializer_class = NewsSerializer


class NewsListThisMonth(generics.ListCreateAPIView):
    '''
        a list of all news this month
    '''
    queryset = News.objects.filter(date__month=month, date__year=year)
    serializer_class = NewsSerializer
