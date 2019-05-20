from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from news.models import (News,)

from news.api.serializers import (NewsSerializer,)

from datetime import date

today = date.today()
day = today.day
month = today.month
year = today.year

class NewsListToday(generics.ListCreateAPIView):
    '''
        news today
    '''
    queryset = News.objects.filter(date__day =  day, date__month = month, date__year = year)
    serializer_class = NewsSerializer

class NewsListThisMonth(generics.ListCreateAPIView):
    '''
        a list of all news this month
    '''
    queryset = News.objects.filter(date__month =  month, date__year = year)
    serializer_class = NewsSerializer
