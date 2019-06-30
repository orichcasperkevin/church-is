from rest_framework import serializers

from groups.api.serializers import ChurchGroupSerializer
from services.models import (ServiceType, Service, ServiceItem, )


class ServiceTypeSerializer(serializers.ModelSerializer):
    church_groups = ChurchGroupSerializer()

    class Meta:
        model = Service
        fields = ('church_groups', 'name')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class ServiceSerializer(serializers.ModelSerializer):
    type = ServiceTypeSerializer()

    class Meta:
        model = Service
        fields = ('type','date', 'venue', 'start', 'end')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class ServiceItemSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = ServiceItem
        fields = ('service', 'action', 'value')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
