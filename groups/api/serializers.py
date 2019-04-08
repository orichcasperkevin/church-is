from rest_framework import serializers
from member.api.serializers import MemberSerializer
from groups.models import (Fellowship,FellowshipMeeting,FellowshipMeetingRoster,FellowshipPhoto,
                           CellGroup,CellGroupMeeting,CellGroupMeetingRoster,CellGroupPhoto,
                           ChurchGroup,ChurchGroup,GroupMeeting,GroupMeetingRoster,GroupPhoto,
                           Ministry,MinistryMeeting,MinistryMeetingRoster,ministryPhoto, )

class FellowshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fellowship
        fields = ('id','name', 'description','fellowship_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class FellowshipMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FellowshipMeeting
        fields = ('id','fellowship', 'host','location','date','fellowship_meeting_attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class CellGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellGroup
        fields = ('id','name', 'description','minister','cell_group_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class CellGroupMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellGroupMeeting
        fields = ('id','cell_group', 'host','location','date','attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class ChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchGroup
        fields = ('id','name', 'description','group_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class ChurchGroupMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMeeting
        fields = ('id','group', 'host','location','date','attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ('id','name', 'description','ministry_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class MinistryMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistryMeeting
        fields = ('id','ministry', 'host','location','date','attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}