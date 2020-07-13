from django.contrib.humanize.templatetags.humanize import intcomma
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
        return  self.message # + "\n" + self.church.domain_ur

class CustomMesageFormatter(ChurchSysMesageFormatter):
    '''
        for sending custom messages after recording member finances
    '''
    def __init__(self,message,schema_name,id,context):
        super().__init__(message,schema_name)#initialize message and schema_name
        self.member = None
        self.first_name = None
        self.this_amount = ''
        self.this_date = ''
        self.recent_giving = ''
        self.this_type = ''
        if context == "All":
            if (id['type'] == "Tithe"):
                try:
                    tithe = Tithe.objects.get(id=id['id'])
                    tithe.notified = True
                    tithe.save()
                    self.member = tithe.member
                    self.this_amount = tithe.amount
                    self.this_date = tithe.date
                    self.this_type = "Tithe"
                    self.recent_giving = "total this month is : " + str(tithe.total_this_month) + ", " +\
                    "total this year is : " + str(tithe.total_this_month)
                except Tithe.DoesNotExist:
                    pass
            else:
                try:
                    offering = Offering.objects.get(id=id['id'])
                    offering.notified = True
                    offering.save()
                    self.member = offering.member
                    self.this_amount = offering.amount
                    self.this_date = offering.date
                    if offering.type:
                        self.this_type = offering.type.name
                    self.recent_giving = "total this month is : " + str(offering.total_this_month) + ", " +\
                    "total this year is : " + str(offering.total_this_month)
                except Offering.DoesNotExist:
                    pass

        if context == "Tithe":
            try:
                tithe = Tithe.objects.get(id=id)
                tithe.notified = True
                tithe.save()
                self.member = tithe.member
                self.this_amount = tithe.amount
                self.this_date = tithe.date
                self.this_type = "Tithe"
                self.recent_giving = "total this month is : " + str(tithe.total_this_month) + ", " +\
                "total this year is : " + str(tithe.total_this_month)
            except Tithe.DoesNotExist:
                print("passed")
                pass

        if context == "Offering":
                try:
                    offering = Offering.objects.get(id=id)
                    offering.notified = True
                    offering.save()
                    self.member = offering.member
                    self.this_amount = offering.amount
                    self.this_date = offering.date
                    if offering.type:
                        self.this_type = offering.type.name
                    self.recent_giving = "total this month is : " + str(offering.total_this_month) + ", " +\
                    "total this year is : " + str(offering.total_this_month)
                except Offering.DoesNotExist:
                    pass

        if context == "Pledge":
            pledge = Pledge.objects.filter(member_id=id).latest('id')
            self.this_amount =  str(pledge.amount) + " towards project " + pledge.project.name
            self.this_date = str(pledge.date)
            self.recent_giving = "amount so far is " + str(pledge.amount_so_far) + ", "+\
            "remaining amount is "+ str(pledge.remaining_amount) + " (" + str(pledge.percentage_funded) +")"

        if context == "Contribution":
            contribution = Contribution.objects.filter(member_id=id).latest('id')
            self.this_amount =  str(contribution.amount) + " towards project " + contribution.project.name
            self.this_date = str(contribution.recorded_at)

        self.replace_with_member_data()


    def replace_with_member_data(self):
        '''
            replace data in '[]' with appropriate member data
        '''
        if self.member:
            self.message = self.message.replace("[name]",self.member.member.get_full_name())
        self.message = self.message.replace("[amount]",intcomma(int(self.this_amount)))
        self.message = self.message.replace("[date]",self.this_date.strftime("%d/%b/%y"))
        self.message = self.message.replace("[type]",self.this_type)

        #capital letters
        if self.member:
            self.message = self.message.replace("[Name]",self.member.member.get_full_name())
        self.message = self.message.replace("[Amount]",intcomma(int(self.this_amount)))
        self.message = self.message.replace("[Date]",self.this_date.strftime("%d/%b/%y"))
        self.message = self.message.replace("[Type]",self.this_type)

    def formated_message(self):
        return  self.message #+   "\n\n" + self.church.domain_url

    def member_id(self):
        return self.member.member.id

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

                if message_formatter.member:

                    messenger.set_message_formatter(message_formatter)
                    receipient = messenger.receipients_phone_numbers([message_formatter.member_id()])
                    if len(receipient):                        
                        messenger.send_message(receipient,message_formatter.formated_message())

                        queryset = Member.objects.filter(member_id=sending_member_id)
                        sending_member = getSerializerData(queryset,MemberSerializer)

                        data = {'sending_member': sending_member, 'app': app, 'message': message, 'website': website}
                        serializer = SmsSerializer(data=data)
                        if serializer.is_valid():
                            created = serializer.save()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
