from rest_framework import serializers

from groups.api.serializers import ChurchGroupSerializer
from services.models import ServiceType, Service, ServiceItem

class ServiceTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id','name','description','start','end')
        extra_kwargs = {'id': {'read_only': True}}

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id','name','description','start','end')
        extra_kwargs = {'id': {'read_only': False}}

class ServiceSerializer(serializers.ModelSerializer):
    type = ServiceTypeSerializer()

    class Meta:
        model = Service
        fields = ('id','type','date', 'venue', 'start', 'end')
        depth = 2
        extra_kwargs = {'id': {'read_only': False}}

class AddServiceSerializer(serializers.ModelSerializer):
    type = ServiceTypeSerializer()
    class Meta:
        model = Service
        fields = ('id','type','date', 'venue', 'start', 'end')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        type = {}
        type_data = validated_data.pop('type')
        type = ServiceType.objects.get(id=type_data['id'])

        service_type = Service.objects.create(type=type, **validated_data)
        return service_type

class ServiceItemSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = ServiceItem
        fields = ('service', 'action', 'value')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        service = {}
        service_data = validated_data.pop('service')
        service = Service.objects.get(id=service_data['id'])

        service = ServiceItem.objects.create(service=service, **validated_data)
        return service
