from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.api.serializers import MemberSerializer
from member.models import Member
from Clients.models import Client

from sms.africastalking.at import ChurchSysMessenger
from sms.api.serializers import SmsSerializer


def getSerializerData(queryset,serializer_class):
    serializer = serializer_class(queryset[0])
    return serializer.data

def formattedMessage(message,sender_id,schema_name,context):
    church = Client.objects.get(schema_name=schema_name)
    church_name = church.name
    sender = Member.objects.get(member_id=sender_id)
    sender_name = sender.member.first_name +" "+ sender.member.last_name

    return church_name.upper() +"\n"+ context.lower() +"\n\n" + message + "\n\n" + sender_name


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

        schema = request.tenant.schema_name
        message = formattedMessage(message,sending_member_id,schema,app)

        messenger = ChurchSysMessenger(schema)
        receipients = messenger.receipients_phone_numbers(receipient_member_ids)
        messenger.send_message(receipients,message)

        queryset = Member.objects.filter(member_id=sending_member_id)
        sending_member = getSerializerData(queryset,MemberSerializer)

        data = {'sending_member': sending_member, 'app': app, 'message': message, 'website': website}
        serializer = SmsSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
