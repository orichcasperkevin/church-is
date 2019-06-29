from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from events.api.serializers import (EventSerializer, ExpectedToAttendEventSerializer, EventAttendanceSerializer)
from events.models import (Event, ExpectedToAttendEvent, EventAttendance)


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

    def get(self, request, id):
        event = ExpectedToAttendEvent.objects.get(event_id=id)
        data = ExpectedToAttendEventSerializer(event).data
        return Response(data)


class EventAttendanceList(APIView):
    '''
        get:
        a list of those attended an event with id <id>
    '''

    def get(self, request, id):
        event = EventAttendance.objects.get(event_id=id)
        data = EventAttendanceSerializer(event).data
        return Response(data)
