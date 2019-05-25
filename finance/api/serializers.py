from rest_framework import serializers

from member.models import Member
from groups.models import ChurchGroup
from member.api.serializers import MemberSerializer
from finance.models import (Offering,Tithe,Income,IncomeType,Expenditure,ExpenditureType,)

class OfferingSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    recorded_by = MemberSerializer()
    class Meta:
        model = Offering
        fields = ('amount','date','anonymous','name_if_not_member','church_group','member',
                    'narration','recorded_by','total_this_month','total_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self,validated_data):
        print(validated_data)
        member_data = validated_data.pop('member')
        if (member_data != None):
            member = {}
            member = Member.objects.get( member_id = member_data["member"]["id"])

        church_group_data = validated_data.pop('church_group')
        if (church_group != None):
            church_group = {}
            church_group = ChurchGroup.objects.get( id = church_group["id"])

        recording_member_data = validated_data.pop('recorded_by')
        recording_member = {}
        recording_member = Member.objects.get( member_id = recording_member_data["member"]["id"])

        offering = Offering.objects.create(member=member, recorded_by=recording_member, **validated_data)
        return tithe

class TitheSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = Tithe
        fields = ('member','amount','date','narration','total_this_month','total_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self,validated_data):

        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get( member_id = member_data["member"]["id"])

        tithe = Tithe.objects.create(member=member,**validated_data)
        return tithe

class IncomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeType
        fields = ('type_name','description','total_this_month','total_this_year')
        extra_kwargs = {'id': {'read_only': True}}

class IncomeSerializer(serializers.ModelSerializer):
    recorded_by = MemberSerializer()
    class Meta:
        model = Income
        fields = ('type','amount','date','narration','recorded_by','total_overall_income_this_month','total_overall_income_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class ExpenditureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenditureType
        fields = ('type_name','description','total_this_month','total_this_year')
        extra_kwargs = {'id': {'read_only': True}}

class ExpenditureSerializer(serializers.ModelSerializer):
    recorded_by = MemberSerializer()
    class Meta:
        model = Expenditure
        fields = ('type','amount','date','narration','recorded_by','total_overall_expenditure_this_month','total_overall_expenditure_this_year')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
