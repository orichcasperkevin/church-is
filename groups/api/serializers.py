from rest_framework import serializers
from member.models import Member,Role
from member.api.serializers import MemberSerializer,RoleSerializer
from groups.models import (Fellowship,FellowshipMembership,FellowshipMeeting,FellowshipMeetingRoster,FellowshipPhoto,
                           CellGroup,CellGroupMembership,CellGroupMeeting,CellGroupMeetingRoster,CellGroupPhoto,
                           ChurchGroup,ChurchGroupMembership,GroupMeeting,GroupMeetingRoster,GroupPhoto,
                           Ministry,MinistryMembership,MinistryMeeting,MinistryMeetingRoster,ministryPhoto, )

class FellowshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fellowship
        fields = ('id','name', 'description','number_of_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}



class FellowshipMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = FellowshipMembership
        fields = ('member','role','date_joined')
        depth = 1

class AddMemberToFellowshipSerializer(serializers.ModelSerializer):
        member = MemberSerializer()
        fellowship = FellowshipSerializer()
        role = RoleSerializer()

        class Meta:
            model = FellowshipMembership
            depth = 1
            fields = ('fellowship','member','role')

        def create(self,validated_data):


            fellowship = {}
            fellowship_data = validated_data.pop('fellowship')
            fellowship = Fellowship.objects.get(**fellowship_data)

            role = {}
            role_data = validated_data.pop('role')
            role = Role.objects.get(**role_data)

            member = {}
            member_data = validated_data.pop('member')
            member = Member.objects.get(id = member_data['id'])

            fellowship_membership = FellowshipMembership.objects.create(fellowship=fellowship,member=member,role=role,**validated_data)
            return fellowship_membership

class FellowshipMeetingSerializer(serializers.ModelSerializer):
    host = MemberSerializer()
    class Meta:
        model = FellowshipMeeting
        fields = ('id','host','location','date','number_of_attendees')
        extra_kwargs = {'id': {'read_only': True}}

class CellGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellGroup
        fields = ('id','name', 'description','number_of_members')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class CellGroupMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = CellGroupMembership
        fields = ('member','role','date_joined')
        depth = 1

class AddMemberToCellGroupSerializer(serializers.ModelSerializer):
        member = MemberSerializer()
        cell_group = CellGroupSerializer()
        role = RoleSerializer()

        class Meta:
            model = CellGroupMembership
            depth = 1
            fields = ('cell_group','member','role')

        def create(self,validated_data):


            cell_group = {}
            cell_group_data = validated_data.pop('cell_group')
            cell_group = CellGroup.objects.get(**cell_group_data)

            role = {}
            role_data = validated_data.pop('role')
            role = Role.objects.get(**role_data)

            member = {}
            member_data = validated_data.pop('member')
            member = Member.objects.get(id = member_data['id'])

            cell_group_membership = CellGroupMembership.objects.create(cell_group=cell_group,member=member,role=role,**validated_data)
            return cell_group_membership

class CellGroupMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellGroupMeeting
        fields = ('id','host','location','date','number_of_attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class ChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchGroup
        fields = ('id','name', 'description','number_of_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class ChurchGroupMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = ChurchGroupMembership
        fields = ('member','role','date_joined')
        depth = 1

class AddMemberToChurchGroupSerializer(serializers.ModelSerializer):
        member = MemberSerializer()
        church_group = ChurchGroupSerializer()
        role = RoleSerializer()

        class Meta:
            model = ChurchGroupMembership
            depth = 1
            fields = ('church_group','member','role')

        def create(self,validated_data):


            church_group = {}
            church_group_data = validated_data.pop('church_group')
            church_group = ChurchGroup.objects.get(**church_group_data)

            role = {}
            role_data = validated_data.pop('role')
            role = Role.objects.get(**role_data)

            member = {}
            member_data = validated_data.pop('member')
            member = Member.objects.get(id = member_data['id'])

            church_group_membership = ChurchGroupMembership.objects.create(church_group=church_group,member=member,role=role,**validated_data)
            return church_group_membership

class ChurchGroupMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMeeting
        fields = ('id','host','location','date','number_of_attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ('id','name', 'description','number_of_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class MinistryMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MinistryMembership
        fields = ('member','role','date_joined')
        depth = 1

class AddMemberToMinistrySerializer(serializers.ModelSerializer):
        member = MemberSerializer()
        ministry = MinistrySerializer()
        role = RoleSerializer()

        class Meta:
            model = MinistryMembership
            depth = 1
            fields = ('ministry','member','role')

        def create(self,validated_data):


            ministry = {}
            ministry_data = validated_data.pop('ministry')
            ministry = Ministry.objects.get(**ministry_data)

            role = {}
            role_data = validated_data.pop('role')
            role = Role.objects.get(**role_data)

            member = {}
            member_data = validated_data.pop('member')
            member = Member.objects.get(id = member_data['id'])

            ministry_membership = MinistryMembership.objects.create(ministry=ministry,member=member,role=role,**validated_data)
            return ministry_membership

class MinistryMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistryMeeting
        fields = ('id','host','location','date','number_of_attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
