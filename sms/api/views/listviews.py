from datetime import date
from rest_framework import generics

from sms.models import SmsReceipients
from sms.api.serializers import SmsReceipientSerializer

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
