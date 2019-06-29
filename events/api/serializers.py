from rest_framework import serializers

from events.models import (Event, ExpectedToAttendEvent, EventAttendance)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'slug', 'date', 'added_on', 'website', 'poster', 'location', 'past')
        extra_kwargs = {'id': {'read_only': True}}


class ExpectedToAttendEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpectedToAttendEvent
        fields = ('id', 'event', 'who_is_coming', 'church_groups_coming', 'fellowships_coming', 'cell_groups_coming',
                  'ministries_coming')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}


class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = ('id', 'event', 'attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}
