from rest_framework import serializers

from member.api.serializers import MemberSerializer
from projects.models import (Project,Pledge,Contribution,PledgePayment)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','church_group','name','start','stop','description','required_amount','raised_amount','remaining_amount','percentage_funded')
        depth = 1
        extra_kwargs = {'id': {'read_only': True}}

class PledgeSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = Pledge
        fields = ('project','member', 'names','phone','amount','recorded_by','recorded_at','amount_so_far','remaining_amount','percentage_funded')
        depth = 1
        extra_kwargs = {'id': {'read_only': True}}

class ContributionSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    recorded_by = MemberSerializer()
    class Meta:
        model = Contribution
        fields = ('project','member','names','phone','amount','recorded_by','recorded_at')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class PledgePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PledgePayment
        fields = ('pledge','payment_amount','payment_recorded_by','payment_recorded_on')
        depth = 1
        extra_kwargs = {'id': {'read_only': True}}
