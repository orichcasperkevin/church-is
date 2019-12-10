# Create your views here.
import json
import requests

from django.views.decorators.csrf import csrf_exempt
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta, date
from base64 import b64decode, b64encode
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from rest_framework.response import Response

from mpesa.models import Stk

# Create your views here.
"""
All mpesa methods
"""

@csrf_exempt
def MpesaAccessToken(request):
    """
    Function to generate token from the consumer secret and key
    """
    consumer_key = 'zN4ebvV2q0oayV8AnBAhWrldLWQxeP7l'
    consumer_secret = 'V9codQwnvdP8gYW1'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    auth = json.loads(r.text)
    token = auth['access_token']
    return token

@csrf_exempt
def STKPush(request,phone,amount):
    """
    Initiate stk push to client. Pass phone number of the client and amount to be billed as parameters.
    Will be called by any the other fucntion that requires to perform a billing and return the data response from safaricom
    """
    api_transaction_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    BusinessShortCode = 174379;
    LipaNaMpesaPasskey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919';
    access_token = MpesaAccessToken(request)
    data = None

    get_now = datetime.now()
    payment_time = get_now.strftime("%Y%m%d%H%M%S")
    to_encode = '{}{}{}'.format(
        BusinessShortCode, LipaNaMpesaPasskey, payment_time)
    payment_password = (b64encode(to_encode.encode('ascii'))).decode("utf-8")

    if access_token:
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": BusinessShortCode,
            "Password": payment_password,
              "Timestamp": payment_time,
              "TransactionType": "CustomerPayBillOnline",
              "Amount": amount,
              "PartyA": phone,
              "PartyB": BusinessShortCode,
              "PhoneNumber": phone,
              "CallBackURL": 'https://cdf67a7a.ngrok.io/mpesa/stk_confirmation/',
              "AccountReference": "redbud",
              "TransactionDesc": 'competition'
        }
        response = requests.post(api_transaction_URL, json=request, headers=headers)
        data = response.text
        print(data)
    else:
        print('access token failed')
    return data

class STKConfirmation(viewsets.GenericViewSet):
    """
    Method that is called back by safaricom in the case of an stk push
    """

    def create(self, request, format=None):
        data = JSONParser().parse(request)
        get_data = data.get('Body').get('stkCallback')
        get_success_data = get_data.get('CallbackMetadata')

        if get_data:
            MerchantRequestID = get_data.get(
                'MerchantRequestID')
            CheckoutRequestID = get_data.get(
                'CheckoutRequestID')
            ResultCode = get_data.get('ResultCode')
            ResultDesc = get_data.get('ResultDesc')

            if get_success_data:
                get_items = get_success_data.get('Item')
                for i in get_items:
                    if i['Name'] == 'Amount':
                        Amount = i.get('Value')
                    elif i['Name'] == 'MpesaReceiptNumber':
                        MpesaReceiptNumber = i.get('Value')
                    elif i['Name'] == 'PhoneNumber':
                        PhoneNumber = i.get('Value')
                    elif i['Name'] == 'Balance':
                        Balance = i.get('Value')
                    elif i['Name'] == 'TransactionDate':
                        TransactionDate = i.get('Value')
                    else:
                        continue

            else:
                Amount = None
                MpesaReceiptNumber = None
                PhoneNumber = None
                Balance = None
                TransactionDate = None

            stk_response = Stk.objects.create(MerchantRequestID=MerchantRequestID,CheckoutRequestID=CheckoutRequestID, \
                            ResultCode=ResultCode,ResultDesc=ResultDesc,Amount=Amount,MpesaReceiptNumber=MpesaReceiptNumber, \
                            PhoneNumber=PhoneNumber,Balance=Balance,TransactionDate=TransactionDate)


        return Response({
            'success': 'Called successfully'

        }, status=status.HTTP_200_OK)
