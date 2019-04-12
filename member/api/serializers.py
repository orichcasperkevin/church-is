from rest_framework import serializers
from django.contrib.auth.models import User
from member.models import (Member,MemberContact,MemberAge,MemberResidence,
                            MemberRole,Role,MemberMaritalStatus,Family,FamilyMembership,)
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email','first_name','last_name')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }

class MemberSerializer(serializers.ModelSerializer):
    member = UserSerializer()
    class Meta:
        model = Member
        fields = ('member','gender')
        extra_kwargs = {'id': {'read_only': False}}

class CreateMemberSerializer(serializers.ModelSerializer):

    member = UserSerializer()
    class Meta:
        model = Member
        fields = ('member','gender')
    def create(self,validated_data):
        member = {}
        member_data = validated_data.pop('member')
        member = User.objects.get(**member_data)

        member = Member.objects.create(member=member,**validated_data)
        return member


class MemberContactSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberContact
        fields = ('id','member', 'postal','phone','contact')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class MemberAgeSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberAge
        fields = ('id','member', 'd_o_b')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class MemberMaritalStatusSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberMaritalStatus
        fields = ('id','member', 'status')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class MemberResidenceSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberResidence
        fields = ('id','member', 'town', 'road', 'street', 'village_estate', 'description')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class FamilySerializer(serializers.ModelSerializer):
    head = MemberSerializer()
    class Meta:
        model = Family
        fields = ('id','name','head','members')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class FamilyMembershipSerializer(serializers.ModelSerializer):
    family = FamilySerializer()
    member = MemberSerializer()
    class Meta:
        model = FamilyMembership
        fields = ('id','family','member')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','role', 'description')
        extra_kwargs = {'id': {'read_only': False}}

class MemberRoleSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberRole
        fields = ('id','member', 'roles')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}
