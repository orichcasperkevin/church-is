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
            },
            'id': {'read_only': False}
        }

class MemberSerializer(serializers.ModelSerializer):
    member = UserSerializer()
    class Meta:
        model = Member
        fields = ('id','member','gender')
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
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self,validated_data):

        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get( member_id = member_data["member"]["id"])

        contact = MemberContact.objects.create(member=member,**validated_data)
        return contact

class MemberAgeSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberAge
        fields = ('id','member', 'd_o_b')
        depth = 1
        extra_kwargs = {'id': {'read_only': True}}

    def create(self,validated_data):

        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get( member_id = member_data["member"]["id"])

        age = MemberAge.objects.create(member=member,**validated_data)
        return age

class MemberMaritalStatusSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberMaritalStatus
        fields = ('id','member', 'status')
        depth = 1
        extra_kwargs = {'id': {'read_only': True}}

    def create(self,validated_data):

        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get( member_id = member_data["member"]["id"])

        marital_status = MemberMaritalStatus.objects.create(member=member,**validated_data)
        return marital_status

class MemberResidenceSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberResidence
        fields = ('id','member', 'town', 'road', 'street', 'village_estate', 'description')
        depth = 1
        extra_kwargs = {'id': {'read_only': True}}

    def create(self,validated_data):

        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get( member_id = member_data["member"]["id"])

        residence = MemberResidence.objects.create(member=member,**validated_data)
        return residence
class FamilySerializer(serializers.ModelSerializer):
    head = MemberSerializer()
    class Meta:
        model = Family
        fields = ('id','name','head','members')
        depth = 2
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
