from rest_framework import serializers

from groups.api.serializers import ChurchGroupSerializer
from member.api.serializers import MemberSerializer
from events.models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'location', 'start', 'end', 'attendees')
        extra_kwargs = {'id': {'read_only': True}}

class AddEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'location', 'start_datetime', 'end_datetime')
        extra_kwargs = {'id': {'read_only': True}}

class GroupAttendingEventSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    group = ChurchGroupSerializer()
    class Meta:
        model = GroupAttendingEvent
        fields = ('event','group')

class AddGroupAttendingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAttendingEvent
        fields = ('event','group')

class MemberThatAttendedEventSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    member = MemberSerializer()
    class Meta:
        model = MemberThatAttendedEvent
        fields = ('member','event')

class AddMemberThatAttendedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberThatAttendedEvent
        fields = ('member','event')
