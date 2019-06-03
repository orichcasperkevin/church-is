from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from member.models import (Member)

from member.api.serializers import (MemberSerializer)
from sms.api.serializers import (SmsSerializer)

from sms.africastalking.at import ChurchSysMessenger

messenger = ChurchSysMessenger("sms app","test member 2")


class addSMS(APIView):
    '''
        add sms
    '''
    def post(self,request):

        sending_member_id = request.data.get("sending_member_id")
        app = request.data.get("app")
        message = request.data.get("message")
        website = request.data.get("website")
        receipient_member_ids = request.data.get("receipient_member_ids")

        receipients = messenger.receipients_phone_numbers(receipient_member_ids)
        messenger.send_message(receipients,message)

        queryset = Member.objects.filter(member_id = sending_member_id)
        member = []
        for member in queryset:
            member = member
        serializer = MemberSerializer(member)
        sending_member = serializer.data

        data = {'sending_member':sending_member,'app':app,'message':message,'website':website}
        serializer = SmsSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
