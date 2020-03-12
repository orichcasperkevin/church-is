from rest_framework import serializers

# import models
from finance.models import *
from member.models import Member
from services.models import Service

#import serializers
from services.api.serializers import ServiceSerializer
from groups.api.serializers import ChurchGroupSerializer
from member.api.serializers import MemberSerializer

class PendingConfirmationSerializer(serializers.ModelSerializer):
    confirming_for = MemberSerializer()
    class Meta:
        model = PendingConfirmation
        fields = ('id','date','confirming_for','confirmation_message','amount','type')

    def create(self, validated_data):
        member_data = validated_data.pop('confirming_for')
        member = {}
        member = Member.objects.get(member_id=member_data["member"]["id"])

        pending_confirmation = PendingConfirmation.objects.create(confirming_for=member,**validated_data)
        return pending_confirmation

class OfferingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferingType
        fields = ('id','name','description')

class OfferingSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    recorded_by = MemberSerializer()

    class Meta:
        model = Offering
        fields = ('type','amount', 'date', 'anonymous', 'name_if_not_member','group', 'member',
                  'service','narration','recorded_by', 'total_this_month', 'total_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}



class AddMemberOfferingSerializer(serializers.ModelSerializer):
    type = OfferingTypeSerializer()
    member = MemberSerializer()
    recorded_by = MemberSerializer()

    class Meta:
        model = Offering
        fields = ('type','amount', 'date', 'anonymous', 'name_if_not_member', 'member',
                  'narration','recorded_by', 'total_this_month', 'total_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        offering_type_data = validated_data.pop('type')
        offering_type = {}
        offering_type = OfferingType.objects.filter(name=offering_type_data["name"]).first()

        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get(member_id=member_data["member"]["id"])

        recording_member_data = validated_data.pop('recorded_by')
        recording_member = {}
        recording_member = Member.objects.get(member_id=recording_member_data["member"]["id"])

        offering = Offering.objects.create(type=offering_type, member=member, recorded_by=recording_member, **validated_data)
        return offering



class addAnonymousOfferingSerializer(serializers.ModelSerializer):
    recorded_by = MemberSerializer()

    class Meta:
        model = Offering
        fields = ('type','amount', 'date', 'group','anonymous', 'name_if_not_member',
                  'narration', 'recorded_by', 'total_this_month', 'total_this_year')
        depth = 2

    def create(self, validated_data):
        recording_member_data = validated_data.pop('recorded_by')
        recording_member = {}
        recording_member = Member.objects.get(member_id=recording_member_data["member"]["id"])

        offering = Offering.objects.create(recorded_by=recording_member, **validated_data)
        return offering

class AddServiceOfferingSerializer(serializers.ModelSerializer):
    '''
        add offering from a service that.
    '''
    recorded_by = MemberSerializer()

    class Meta:
        model = Offering
        fields = ('type','amount', 'date','service','group','narration', 'recorded_by',)

    def create(self, validated_data):

        recording_member_data = validated_data.pop('recorded_by')
        recording_member = {}
        recording_member = Member.objects.get(member_id=recording_member_data["member"]["id"])

        offering = Offering.objects.create(recorded_by=recording_member, **validated_data)
        return offering


class TitheSerializer(serializers.ModelSerializer):
    member = MemberSerializer()

    class Meta:
        model = Tithe
        fields = ('member', 'amount', 'date','service','group', 'narration', 'recorded_by', 'total_this_month', 'total_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class AddTitheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tithe
        fields = ('member', 'amount', 'date','service','group', 'narration', 'recorded_by', 'total_this_month', 'total_this_year')

class IncomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeType
        fields = ('id', 'type_name', 'description', 'total_this_month', 'total_this_year')
        extra_kwargs = {'id': {'read_only': True}}


class IncomeSerializer(serializers.ModelSerializer):
    recorded_by = MemberSerializer()
    type = IncomeTypeSerializer()

    class Meta:
        model = Income
        fields = ('type', 'amount', 'date', 'narration', 'recorded_by', 'total_overall_income_this_month',
                  'total_overall_income_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        recording_member_data = validated_data.pop('recorded_by')
        member = {}
        member = Member.objects.get(member_id=recording_member_data["member"]["id"])

        income_type_data = validated_data.pop('type')
        income_type = IncomeType.objects.get(**income_type_data)

        income = Income.objects.create(recorded_by=member, type=income_type, **validated_data)
        return income


class ExpenditureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenditureType
        fields = ('id','type_name', 'description', 'total_this_month', 'total_this_year')
        extra_kwargs = {'id': {'read_only': True}}


class ExpenditureSerializer(serializers.ModelSerializer):
    recorded_by = MemberSerializer()
    type = ExpenditureTypeSerializer()

    class Meta:
        model = Expenditure
        fields = ('type', 'amount', 'date', 'narration', 'recorded_by')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        recording_member_data = validated_data.pop('recorded_by')
        member = {}
        member = Member.objects.get(member_id=recording_member_data["member"]["id"])

        expenditure_type_data = validated_data.pop('type')
        expenditure_type = ExpenditureType.objects.get(**expenditure_type_data)

        expenditure = Expenditure.objects.create(recorded_by=member, type=expenditure_type, **validated_data)
        return expenditure
