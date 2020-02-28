import africastalking
from decouple import config

from member.models import MemberContact
from sms.models import SmsReceipients, Sms
from Clients.models import ClientDetail, ChurchSMSCredentials
from tenant_schemas.utils import schema_context

CREDIT_PER_SMS = 1.00
'''
    this class adapts africastalking api to the sms app.
'''


class ChurchSysMessenger():
    def __init__(self, schema, message_formatter):
        self.schema = schema #what schema to use
        self.message_formatter = message_formatter
        username = ''
        api_key = ''

        if schema[slice(0,4)] == "demo":
            username = config('DEMO_AFRICAS_TALKING_USERNAME')
            api_key = config('DEMO_AFRICAS_TALKING_API_KEY')
        else:
            credentials = ChurchSMSCredentials.objects.filter(church__schema_name=schema)[0]
            username = credentials.at_username
            api_key = credentials.at_api_key
        #initialize africastalking
        africastalking.initialize(username, api_key)
        self.sms_service = africastalking.SMS


    def receipients_phone_numbers(self, receipient_member_ids):
        '''
            get the a list of phone numbers from a list of receipient ids
        '''
        with schema_context(self.schema):
            phone_numbers = []
            for data in receipient_member_ids:
                try:
                    contact = MemberContact.objects.get(member__member_id = data)
                    member_phone_number = contact.phone
                    if not member_phone_number:
                        continue
                    if member_phone_number[0] == '0':
                        member_phone_number = member_phone_number.replace('0','+254',1)
                    if member_phone_number[:3] == '254':
                        member_phone_number = member_phone_number.replace('254','+254',1)
                    phone_numbers.append(member_phone_number)
                except MemberContact.DoesNotExist:
                    pass #TODO add a mechanism to generate this as a send sms error
            return phone_numbers

    def record_members_who_received_sms(self, sent_messages):
        '''
            if message was sent, record the members who received it and on what status
        '''
        with schema_context(self.schema):
            for message in sent_messages['SMSMessageData']['Recipients']:
                try:
                    contact = MemberContact.objects.filter(phone__contains=message['number'][slice(4,13)])[0]
                    member = contact.member
                    sms = Sms.objects.latest('id')
                    received_sms = SmsReceipients.objects.create(sms=sms, receipient=member, cost=message['cost'], status=message['status'])
                except MemberContact.DoesNotExist:
                    pass  #TODO add a mechanism to generate this as a send sms error

    def on_finish(self, error, response):
        '''
            callback function called on completion of the thread on which send_message() is running
        '''
        if error is not None:
            raise error
        self.record_members_who_received_sms(response)

    def send_message(self, receipients, message):
        '''
            send message
        '''
        message = self.message_formatter.formated_message()
        self.sms_service.send(message, receipients, callback=self.on_finish)
