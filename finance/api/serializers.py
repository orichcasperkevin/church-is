from rest_framework import serializers

from finance.models import (Offering, GroupOffering, Tithe, Income, IncomeType, Expenditure, ExpenditureType, )
from groups.api.serializers import ChurchGroupSerializer
from member.api.serializers import MemberSerializer
from member.models import Member


class OfferingSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    recorded_by = MemberSerializer()

    class Meta:
        model = Offering
        fields = ('amount', 'date', 'anonymous', 'name_if_not_member', 'church_group', 'member',
                  'narration', 'recorded_by', 'total_this_month', 'total_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get(member_id=member_data["member"]["id"])

        recording_member_data = validated_data.pop('recorded_by')
        recording_member = {}
        recording_member = Member.objects.get(member_id=recording_member_data["member"]["id"])

        offering = Offering.objects.create(member=member, recorded_by=recording_member, **validated_data)
        return offering


class addAnonymousOfferingSerializer(serializers.ModelSerializer):
    recorded_by = MemberSerializer()

    class Meta:
        model = Offering
        fields = ('amount', 'date', 'anonymous', 'name_if_not_member', 'church_group',
                  'narration', 'recorded_by', 'total_this_month', 'total_this_year')
        depth = 2

    def create(self, validated_data):
        recording_member_data = validated_data.pop('recorded_by')
        recording_member = {}
        recording_member = Member.objects.get(member_id=recording_member_data["member"]["id"])

        offering = Offering.objects.create(recorded_by=recording_member, **validated_data)
        return offering


class GroupOfferingSerializer(serializers.ModelSerializer):
    church_group = ChurchGroupSerializer()
    offering = OfferingSerializer()

    class Meta:
        model = GroupOffering
        fields = ('church_group', 'offering',)
        depth = 2


class TitheSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    recorded_by = MemberSerializer()

    class Meta:
        model = Tithe
        fields = ('member', 'amount', 'date', 'narration', 'recorded_by', 'total_this_month', 'total_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get(member_id=member_data["member"]["id"])

        recording_member_data = validated_data.pop('recorded_by')
        recording_member = {}
        recording_member = Member.objects.get(member_id=recording_member_data["member"]["id"])

        tithe = Tithe.objects.create(member=member, recorded_by=recording_member, **validated_data)
        return tithe


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
        fields = ('type_name', 'description', 'total_this_month', 'total_this_year')
        extra_kwargs = {'id': {'read_only': True}}


class ExpenditureSerializer(serializers.ModelSerializer):
    recorded_by = MemberSerializer()
    type = ExpenditureTypeSerializer()

    class Meta:
        model = Expenditure
        fields = ('type', 'amount', 'date', 'narration', 'recorded_by', 'total_overall_expenditure_this_month',
                  'total_overall_expenditure_this_year')
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
