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


class MesageFormatter():
    '''
        future proofing so that i can use the class to apply custom formats.
    '''
    def __init__(self,message,sender_id,schema_name,context):
        self.context = context
        self.message = message
        church = Client.objects.get(schema_name=schema_name)
        self.church_domain = church.domain_url

    def formated_message(self):
        return  self.message \
                +   "\n " + self.church_domain
                #  self.church_name.upper()\
                 #+   "\n"+ self.context.lower()\
                 #+   "\n" + self.message + "\n"\


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
        message_formatter = MesageFormatter(message,sending_member_id,schema,app)

        messenger = ChurchSysMessenger(schema,message_formatter)
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
