from rest_framework import serializers


from member.models import (Member,)
from member.api.serializers import MemberSerializer
from projects.models import (Project,Pledge,Contribution,PledgePayment)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','church_group','name','start','stop','description','required_amount','raised_amount','remaining_amount','percentage_funded')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class PledgeSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    project = ProjectSerializer()
    recorded_by = MemberSerializer()
    class Meta:
        model = Pledge
        fields = ('id','project','member', 'names','phone','amount','date','recorded_by','recorded_at','amount_so_far','remaining_amount','percentage_funded')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

    def create(self,validated_data):


        project_data = validated_data.pop('project')
        project = {}
        project = Project.objects.get( id = project_data["id"])

        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get( id = member_data["member"]["id"])

        recording_member_data = validated_data.pop('recorded_by')
        recorded_by = {}
        recorded_by = Member.objects.get( id = member_data["member"]["id"])

        pledge = Pledge.objects.create(project=project,member=member,recorded_by=recorded_by,**validated_data)
        return pledge

class ContributionSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    recorded_by = MemberSerializer()
    project = ProjectSerializer()
    class Meta:
        model = Contribution
        fields = ('project','anonymous','member','names','phone','amount','recorded_by','recorded_at')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

    def create(self,validated_data):


        project_data = validated_data.pop('project')
        project = {}
        project = Project.objects.get( id = project_data["id"])

        member_data = validated_data.pop('member')
        member = {}
        member = Member.objects.get( id = member_data["member"]["id"])

        recording_member_data = validated_data.pop('recorded_by')
        recorded_by = {}
        recorded_by = Member.objects.get( id = member_data["member"]["id"])

        contribution = Contribution.objects.create(project=project,member=member,recorded_by=recorded_by,**validated_data)
        return contribution


class PledgePaymentSerializer(serializers.ModelSerializer):
    pledge = PledgeSerializer()
    payment_recorded_by = MemberSerializer()
    class Meta:
        model = PledgePayment
        fields = ('pledge','payment_amount','payment_recorded_by','payment_recorded_on')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

    def create(self,validated_data):


        pledge_data = validated_data.pop('pledge')
        pledge = {}
        pledge = Pledge.objects.get( id = pledge_data["id"])

        recording_member_data = validated_data.pop('payment_recorded_by')
        payment_recorded_by = {}
        payment_recorded_by = Member.objects.get( id = recording_member_data["member"]["id"])

        pledge_payment = PledgePayment.objects.create(pledge=pledge,payment_recorded_by=payment_recorded_by,**validated_data)
        return pledge_payment
