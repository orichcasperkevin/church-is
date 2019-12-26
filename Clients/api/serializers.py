from rest_framework import serializers

from Clients.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'created_on', 'paid' ,'paid_until', 'on_trial')

class ClientDetailSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    class Meta:
        model = ClientDetail
        fields = ('client','first_name','last_name','ID_number','phone_number','city_or_town','location_description','website')
