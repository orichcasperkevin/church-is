from rest_framework.views import APIView
from rest_framework.response import Response

from events.models import GroupAttendingEvent,MemberThatAttendedEvent
from events.api.serializers import EventSerializer,GroupAttendingEventSerializer,MemberThatAttendedEventSerializer

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
