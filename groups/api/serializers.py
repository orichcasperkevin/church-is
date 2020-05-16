from rest_framework import serializers

from groups.models import GroupOfChurchGroups, ChurchGroup, ChurchGroupMembership
from member.api.serializers import MemberSerializer, RoleSerializer
from member.models import Member, Role

class GroupOfChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupOfChurchGroups
        fields = ('id', 'name', 'description', 'number_of_groups')
        extra_kwargs = {'id': {'read_only': True}}


class ChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchGroup
        fields = ('id', 'group', 'name', 'description','number_of_members')
        extra_kwargs = {'id': {'read_only': True}}


class ChurchGroupMembershipSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='member.member.id')
    member_full_name = serializers.CharField(source='member.member.get_full_name')
    member_gender = serializers.CharField(source='member.gender')
    role_name = serializers.CharField(source='role.role')
    class Meta:
        model = ChurchGroupMembership
        fields = ('id', 'church_group', 'member', 'role', 'date_joined',
                  'user_id','member_full_name','member_gender','role_name')
