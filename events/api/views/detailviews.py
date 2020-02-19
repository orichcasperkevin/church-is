from rest_framework.views import APIView
from rest_framework.response import Response

from events.models import Event,GroupAttendingEvent,MemberThatAttendedEvent
from events.api.serializers import EventSerializer,GroupAttendingEventSerializer,MemberThatAttendedEventSerializer

class GetEvent(APIView):
    '''
        get an event using its id.
    '''
    def get(self,request,event_id):
        event = Event.objects.filter(id=event_id)
        data = EventSerializer(event,many=True).data
        return Response(data)

class GetEventWhereTitleLikePattern(APIView):
    '''
        get:
        returns a list of events whose title contains the string pattern described in the slug parameter
    '''

    def get(self, request, pattern):
        result = Event.objects.filter(title__icontains=pattern).order_by('-start_datetime')[:10]
        data = EventSerializer(result, many=True).data
        return Response(data)


class GetGroupsAttendingEvent(APIView):
    '''
        get group attending event.
    '''
    def get(self,request,event_id):
        groups = GroupAttendingEvent.objects.filter(event_id=event_id)[:1]
        data = GroupAttendingEventSerializer(groups, many=True).data
        return Response(data)

class GetEventsAttendedByGroup(APIView):
    '''
    get:
    get the events attended by a group
    '''

    def get(self, request, group_id):
        group = GroupAttendingEvent.objects.filter(group_id=group_id)[:50]
        data = GroupAttendingEventSerializer(group, many=True).data
        return Response(data)

class GetMembersThatAttendedEvent(APIView):
    '''
        get:
        get the members that attended an event.
    '''
    def get(self,request,event_id):
        members = MemberThatAttendedEvent.objects.filter(event_id=event_id)
        data = MemberThatAttendedEventSerializer(members, many=True).data
        return Response(data)

class GetAttendanceForMember(APIView):
    '''
        get:
        attendance for members.
    '''
    def get(self,request,member_id):
        member_attendance = MemberThatAttendedEvent.objects.filter(member__member_id=member_id)
        data = MemberThatAttendedEventSerializer(member_attendance, many=True).data
        return Response(data)
