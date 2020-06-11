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

class ModeOfPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeOfPayment
        fields = ('id','name')

class OfferingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferingType
        fields = ('id','name','description')

class OfferingSerializer(serializers.ModelSerializer):
    mode_of_payment_name = serializers.CharField(source='mode_of_payment.name',default=None)

    user_id = serializers.IntegerField(source='member.member.id',default=None)
    member_full_name = serializers.CharField(source='member.member.get_full_name',default=None)
    member_gender = serializers.CharField(source='member.gender',default=None)

    service_type_name = serializers.CharField(source='service.type.name',default=None)
    service_date = serializers.DateField(source='service.date',default=None)

    group_id = serializers.IntegerField(source='group.id',default=None)
    group_name = serializers.CharField(source='group.name',default=None)

    class Meta:
        model = Offering
        fields = ('type','amount','mode_of_payment','mode_of_payment_name', 'date',
                  'name_if_not_member','phone_if_not_member',
                  'group', 'member',
                  'service','narration','recorded_by', 'total_this_month', 'total_this_year',
                  'user_id','member_full_name','member_gender','service_type_name',
                  'service_date','group_id','group_name')

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
    mode_of_payment_name = serializers.CharField(source='mode_of_payment.name',default=None)

    user_id = serializers.IntegerField(source='member.member.id',default=None)
    member_full_name = serializers.CharField(source='member.member.get_full_name',default=None)
    member_gender = serializers.CharField(source='member.gender',default=None)

    service_type_name = serializers.CharField(source='service.type.name',default=None)
    service_date = serializers.DateField(source='service.date',default=None)

    group_id = serializers.IntegerField(source='group.id',default=None)
    group_name = serializers.CharField(source='group.name',default=None)
    class Meta:
        model = Tithe
        fields = ('member', 'amount','mode_of_payment','mode_of_payment_name',
                  'name_if_not_member','phone_if_not_member'
                  'date','service','group', 'narration',
                  'recorded_by', 'total_this_month', 'total_this_year',
                  'user_id','member_full_name','member_gender','service_type_name',
                  'service_date','group_id','group_name')


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

class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV
        fields = "__all__"
