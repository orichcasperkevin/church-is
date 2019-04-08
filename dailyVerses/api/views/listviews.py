from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from dailyVerses.models import (Verse)
from dailyVerses.api.serializers import (VerseSerializer,)

class VerseList(generics.ListCreateAPIView):
    '''
        get:
        a list of verses
    '''
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer