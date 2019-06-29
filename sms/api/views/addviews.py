from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.api.serializers import (MemberSerializer)
from member.models import (Member)
from sms.africastalking.at import ChurchSysMessenger
from sms.api.serializers import (SmsSerializer)

messenger = ChurchSysMessenger("sms app", "test member 2")


class addSMS(APIView):
    '''
        add sms
    '''

    def post(self, request):

        sending_member_id = request.data.get("sending_member_id")
        app = request.data.get("app")
        message = request.data.get("message")
        website = request.data.get("website")
        receipient_member_ids = request.data.get("receipient_member_ids")

<<<<<<< HEAD
        receipients = messenger.receipients_phone_numbers(receipient_member_ids)        
        messenger.send_message(receipients,message)
=======
        receipients = messenger.receipients_phone_numbers(receipient_member_ids)
        messenger.send_message(receipients, message)
>>>>>>> 9dfcfe161ebeca409d9209e37a98a5c81235dcb8

        queryset = Member.objects.filter(member_id=sending_member_id)
        member = []
        for member in queryset:
            member = member
        serializer = MemberSerializer(member)
        sending_member = serializer.data

        data = {'sending_member': sending_member, 'app': app, 'message': message, 'website': website}
        serializer = SmsSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
