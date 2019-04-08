from rest_framework import serializers
from django.contrib.auth.models import User
from member.models import (Member,MemberContact,MemberAge,MemberResidence,
                            MemberRole,Role,MemberMaritalStatus,Family,FamilyMember,)
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email',)
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }

class MemberSerializer(serializers.ModelSerializer):
    member = UserSerializer()
    class Meta:
        model = Member
        fields = ('member',)
        extra_kwargs = {'id': {'read_only': False}}


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
        fields = ('id','name','head')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class FamilyMemberSerializer(serializers.ModelSerializer):
    family = FamilySerializer()
    member = MemberSerializer()
    class Meta:
        model = FamilyMember
        fields = ('id','family','member')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','role', 'description')
        extra_kwargs = {'id': {'read_only': False}}

class MemberRoleSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    member = MemberSerializer()
    class Meta:
        model = MemberRole
        fields = ('id','member', 'role')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}