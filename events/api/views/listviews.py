from rest_framework import generics

from events.api.serializers import EventSerializer

from events.models import Event

class EventsList(generics.ListCreateAPIView):
    '''
        a list of events
    '''
    queryset = Event.objects.all().order_by('-start_datetime')[:50]
    serializer_class = EventSerializer
