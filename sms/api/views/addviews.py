from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.api.serializers import MemberSerializer
from member.models import Member
from finance.models import Tithe,Offering
from projects.models import Pledge,Contribution

from sms.africastalking.at import ChurchSysMessenger,ChurchSysMesageFormatter
from sms.api.serializers import SmsSerializer

def getSerializerData(queryset,serializer_class):
    serializer = serializer_class(queryset[0])
    return serializer.data


class MesageFormatter(ChurchSysMesageFormatter):
    '''
        how this message is formated
    '''
    def formated_message(self):
        return  self.message + "\n" + self.church.domain_url

class CustomMesageFormatter(ChurchSysMesageFormatter):
    '''
        for sending custom messages after recording member finances
    '''
    def __init__(self,message,schema_name,member_id,context):
        super().__init__(message,schema_name)#initialize message and schema_name
        self.member = Member.objects.get(member_id=member_id)
        self.first_name = self.member.member.first_name
        self.this_amount = ''
        self.this_date = ''
        self.recent_giving = ''

        if context == "Tithe":
            tithe = Tithe.objects.filter(member=self.member).latest('id')
            self.this_amount = str(tithe.amount)
            self.this_date = str(tithe.date)
            self.recent_giving = "total this month is : " + str(tithe.total_this_month) + ", " +\
            "total this year is : " + str(tithe.total_this_month)

        if context == "Offering":
            offering = Offering.objects.filter(member=self.member).latest('id')
            self.this_amount = str(offering.amount)
            self.this_date = str(offering.date)
            self.recent_giving = "total this month is : " + str(offering.total_this_month) + ", " +\
            "total this year is : " + str(offering.total_this_month)

        if context == "Pledge":
            pledge = Pledge.objects.filter(member=self.member).latest('id')
            self.this_amount =  str(pledge.amount) + " towards project " + pledge.project.name
            self.this_date = str(pledge.date)
            self.recent_giving = "amount so far is " + str(pledge.amount_so_far) + ", "+\
            "remaining amount is "+ str(pledge.remaining_amount) + " (" + str(pledge.percentage_funded) +")"

        if context == "Contribution":
            contribution = Contribution.objects.filter(member=self.member).latest('id')
            self.this_amount =  str(contribution.amount) + " towards project " + contribution.project.name
            self.this_date = str(contribution.recorded_at)

        self.replace_with_member_data()


    def replace_with_member_data(self):
        '''
            replace data in '[]' with appropriate member data
        '''
        self.message = self.message.replace("[name]",self.first_name)
        self.message = self.message.replace("[amount]",self.this_amount)    
        self.message = self.message.replace("[date]",self.this_date)

    def formated_message(self):
        return  self.message +   "\n\n" + self.church.domain_url

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
        message_formatter = MesageFormatter(message,schema)

        messenger = ChurchSysMessenger(schema)
        messenger.set_message_formatter(message_formatter)
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


class addCustomSMS(APIView):
    '''
        custom sms for every member it is sent to
    '''

    def post(self, request):
        sending_member_id = request.data.get("sending_member_id")
        app = request.data.get("app")
        message = request.data.get("message")
        website = request.data.get("website")
        context = request.data.get("context")
        receipient_member_ids = request.data.get("receipient_member_ids")

        schema = request.tenant.schema_name
        messenger = ChurchSysMessenger(schema)
        try:
            for id in receipient_member_ids:
                #create a message formater.
                message_formatter = CustomMesageFormatter(message,schema,id,context)

                messenger.set_message_formatter(message_formatter)
                receipient = messenger.receipients_phone_numbers([id])
                messenger.send_message(receipient,message)

                queryset = Member.objects.filter(member_id=sending_member_id)
                sending_member = getSerializerData(queryset,MemberSerializer)

                data = {'sending_member': sending_member, 'app': app, 'message': message_formatter.formated_message(), 'website': website}
                serializer = SmsSerializer(data=data)
                if serializer.is_valid():
                    created = serializer.save()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:#Exception as e:
            #raise
            return Response(status=status.HTTP_400_BAD_REQUEST)
