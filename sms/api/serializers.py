from rest_framework import serializers

from groups.api.serializers import ChurchGroupSerializer
from member.api.serializers import MemberSerializer
from member.models import Member
from sms.models import (Sms, SmsReceipients, SmsReceipientGroups)


class SmsSerializer(serializers.ModelSerializer):
    sending_member = MemberSerializer()

    class Meta:
        model = Sms
        fields = ('id', 'app', 'message', 'sending_member', 'receipients', 'church_groups',
                  'date', 'website')
        depth = 2

        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        member_data = validated_data.pop('sending_member')
        member = {}
        member = Member.objects.get(member_id=member_data["member"]["id"])

        sms = Sms.objects.create(sending_member=member, **validated_data)
        return sms


class SmsReceipientSerializer(serializers.ModelSerializer):
    receipient = MemberSerializer()
    sms = SmsSerializer()

    class Meta:
        model = SmsReceipients
        fields = ('sms', 'receipient')
        depth = 1


class SmsReceipientGroupsSerializer(serializers.ModelSerializer):
    receipient_group = ChurchGroupSerializer()
    sms = SmsSerializer()

    class Meta:
        model = SmsReceipientGroups
        fields = ('sms', 'receipient_group')
        depth = 1
