from rest_framework import serializers
from member.api.serializers import MemberSerializer
from groups.models import (Fellowship,FellowshipMembership,FellowshipMeeting,FellowshipMeetingRoster,FellowshipPhoto,
                           CellGroup,CellGroupMembership,CellGroupMeeting,CellGroupMeetingRoster,CellGroupPhoto,
                           ChurchGroup,ChurchGroupMembership,GroupMeeting,GroupMeetingRoster,GroupPhoto,
                           Ministry,MinistryMembership,MinistryMeeting,MinistryMeetingRoster,ministryPhoto, )

class FellowshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fellowship
        fields = ('id','name', 'description','number_of_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class FellowshipMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = FellowshipMembership
        fields = ('member','role','date_joined')
        depth = 1

class FellowshipMeetingSerializer(serializers.ModelSerializer):
    host = MemberSerializer()
    class Meta:
        model = FellowshipMeeting
        fields = ('id','host','location','date','number_of_attendees')
        extra_kwargs = {'id': {'read_only': False}}

class CellGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellGroup
        fields = ('id','name', 'description','minister','number_of_members')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class CellGroupMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = FellowshipMembership
        fields = ('member','role','date_joined')
        depth = 1

class CellGroupMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellGroupMeeting
        fields = ('id','host','location','date','number_of_attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class ChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchGroup
        fields = ('id','name', 'description','number_of_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class ChurchGroupMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = ChurchGroupMembership
        fields = ('member','role','date_joined')
        depth = 1

class ChurchGroupMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMeeting
        fields = ('id','host','location','date','number_of_attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ('id','name', 'description','number_of_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class MinistryMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MinistryMembership
        fields = ('member','role','date_joined')
        depth = 1

class MinistryMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistryMeeting
        fields = ('id','host','location','date','number_of_attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}
