
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from events.models import (Event,ExpectedToAttendEvent,EventRoster,EventAttendance)
from events.api.serializers import (EventSerializer,ExpectedToAttendEventSerializer,EventAttendanceSerializer)

class EventList(generics.ListCreateAPIView):
    '''
        get:
        a list of events
    '''
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ExpectedToAttendEventList(APIView):
    '''
        get:
        a list of those expected to attend an event with id <id>
    '''
    def get(self,request,id):
        event = ExpectedToAttendEvent.objects.get(event_id = id)
        data = ExpectedToAttendEventSerializer(event).data
        return Response(data)

class EventAttendanceList(APIView):
    '''
        get:
        a list of those attended an event with id <id>
    '''
    def get(self,request,id):
        event = EventAttendance.objects.get(event_id = id)
        data = EventAttendanceSerializer(event).data
        return Response(data)
