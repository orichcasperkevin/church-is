from rest_framework import serializers

from member.models import Member
from groups.api.serializers import ChurchGroupSerializer
from services.models import (Service,ServiceItem,)

class ServiceSerializer(serializers.ModelSerializer):
    church_group = ChurchGroupSerializer()
    class Meta:
        model = Service
        fields = ('church_group','name','date')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class ServiceItemSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    class Meta:
        model = ServiceItem
        fields = ('service','action','value','start','end')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
