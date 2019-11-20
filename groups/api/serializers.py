from rest_framework import serializers

from groups.models import GroupOfChurchGroups, ChurchGroup, ChurchGroupMembership, GroupMeeting
from member.api.serializers import MemberSerializer, RoleSerializer
from member.models import Member, Role

class GroupOfChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupOfChurchGroups
        fields = ('id', 'name', 'description', 'number_of_groups')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class ChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchGroup
        fields = ('id', 'name', 'description', 'number_of_members',)
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class AddChurchGroupSerializer(serializers.ModelSerializer):
    group = GroupOfChurchGroupSerializer()
    class Meta:
        model = ChurchGroup
        fields = ('id', 'group', 'name', 'description')
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        group = {}
        group_data = validated_data.pop('group')
        group = GroupOfChurchGroups.objects.get(**group_data)

        group = ChurchGroup.objects.create(group=group, **validated_data)
        return group

class ChurchGroupMembershipSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = ChurchGroupMembership
        fields = ('id', 'church_group', 'member', 'role', 'date_joined')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}


class AddMemberToChurchGroupSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    church_group = ChurchGroupSerializer()
    role = RoleSerializer()

    class Meta:
        model = ChurchGroupMembership
        depth = 1
        fields = ('church_group', 'member', 'role')

    def create(self, validated_data):
        church_group = {}
        church_group_data = validated_data.pop('church_group')
        church_group = ChurchGroup.objects.get(**church_group_data)

        role = {}
        role_data = validated_data.pop('role')
        role = Role.objects.get(**role_data)

        member = {}
        member_data = validated_data.pop('member')
        member = Member.objects.get(id=member_data['id'])

        church_group_membership = ChurchGroupMembership.objects.create(church_group=church_group, member=member,
                                                                       role=role, **validated_data)
        return church_group_membership


class ChurchGroupMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMeeting
        fields = ('id', 'host', 'location', 'date', 'number_of_attendees')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
