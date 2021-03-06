from rest_framework import serializers
from Clients.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'domain_url','created_on', 'paid' ,'paid_until', 'on_trial')

class ClientDetailSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    class Meta:
        model = ClientDetail
        fields = ('client','first_name','last_name','ID_number','phone_number','domain_url',
                    'city_or_town','location_description','website','church_code',
                    'number_of_members','number_of_sms','created_on','credit',
                    'apprx_number_of_days_left','tier','site_visitors')

class ChurchSMSCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchSMSCredentials
        fields = ('at_username','at_api_key','at_mpesa_acc_no','at_mpesa_paybill')

class ChurchLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchLogo
        fields = ('church','logo')

class ChurchAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchAbout
        fields = ('church','about')

class ChurchStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchStatement
        fields = ('church','mission','vision')

class ChurchCoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchCoreValue
        fields = ('church','value')

class ChurchPeriodicThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchPeriodicTheme
        fields = ('church','theme','description','start','end')
