from datetime import date
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from sms.models import SmsReceipients
from sms.api.serializers import SmsReceipientSerializer

from sms.africastalking.at import ChurchSysMessenger
from .addviews import CustomMesageFormatter

today = date.today()
day = today.day
month = today.month
year = today.year

class SmsList(generics.ListCreateAPIView):
    '''
        a list of sms sent this month
    '''
    queryset = SmsReceipients.objects.filter(sms__date__year=year,sms__date__month=month).order_by('-sms__date')[:100]
    serializer_class = SmsReceipientSerializer

class ExtractCustomMessage(APIView):
    def get(self,request):
        message = request.data.get("message")
        receipient_id = request.data.get("receipient_id")
        context = request.data.get("context")
        schema = request.tenant.schema_name
        message_formatter = CustomMesageFormatter(message,schema,receipient_id,context)
        return Response(message_formatter.formated_message())

class SMSCreditBalance(APIView):
    def get(self,request):
        schema = request.tenant.schema_name
        messenger = ChurchSysMessenger(schema)
        data = messenger.get_sms_credit_balance()

        return Response(data)
