from rest_framework import serializers

from groups.api.serializers import ChurchGroupSerializer
from services.models import (ServiceType, Service, ServiceItem, )


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id','name','description','church_groups')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

class ServiceSerializer(serializers.ModelSerializer):
    type = ServiceTypeSerializer()

    class Meta:
        model = Service
        fields = ('id','type','date', 'venue', 'start', 'end')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class ServiceItemSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = ServiceItem
        fields = ('service', 'action', 'value')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
