from datetime import datetime

from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView

from events.api.serializers import AddEventSerializer,AddGroupAttendingEventSerializer,AddMemberThatAttendedEventSerializer

from events.models import Event

class AddEvent(APIView):
    '''
        add an event
    '''
    def post(self,request):
        title = request.data.get("title")
        description = request.data.get("description")
        location = request.data.get("location")
        #start
        start_date = request.data.get("start_date")
        start_time = request.data.get("start_time")

        start_str = start_date + " " + start_time
        start_datetime = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        #end
        end_date = request.data.get("end_date")
        end_time = request.data.get("end_time")

        end_str = end_date + " " + end_time
        end_datetime = datetime.strptime(end_str, "%Y-%m-%d %H:%M")

        data={'title':title, 'description':description, 'location':location,
                'start_datetime':start_datetime, 'end_datetime':end_datetime}

        serializer = AddEventSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddGroupAttendingEvent(APIView):
    '''
    post:
    add group that is expected to attend the event
    '''
    def post(self,request):
        group = request.data.get("group_id")
        event = request.data.get("event_id")

        data={'group':group, 'event':event,}

        serializer = AddGroupAttendingEventSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecordMemberThatAttendedEvent(APIView):
    '''
    post:
    record a member that attended an event
    '''
    def post(self,request):
        event = request.data.get("event_id")

        member = request.data.get("member_id")
        data={'member':member, 'event':event,}
        serializer = AddMemberThatAttendedEventSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
