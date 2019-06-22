
import africastalking

from decouple import config

from member.models import MemberContact
from sms.models import SmsReceipients,Sms
# Initialize SDK
username = config('AFRICAS_TALKING_USERNAME')
api_key = config('AFRICAS_TALKING_API_KEY')
sender_id = config('AFRICAS_TALKING_SENDER_ID')

africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS
'''
    this class adapts africastalking api to the sms app.
'''
class ChurchSysMessenger():
    def __init__(self, sender_app,sending_member):
        self.sender_app = sender_app
        self.sending_member = sending_member

    def receipients_phone_numbers(self,receipient_member_ids):
        '''
            get the a list of phone numbers from a list of receipient ids
        '''
        phone_numbers = []
        for data in receipient_member_ids:
            try:
                contact = MemberContact.objects.get(member_id = data)
                member_phone_number = contact.phone
                phone_numbers.append(member_phone_number)
            except:
                return "error getting phone numbers"
        return phone_numbers

    def record_members_who_received_sms(self,sent_messages):
        '''
            if message was sent, record the members who received it and on what status
        '''
        for data in sent_messages['SMSMessageData']['Recipients']:
            contact = MemberContact.objects.get(phone = data['number'])
            member = contact.member
            sms = Sms.objects.latest('id')

            SmsReceipients.objects.create(sms=sms,receipient=member,cost=data['cost'], status=data['status'])

    def on_finish(self,error, response):
        '''
            callback function called on completion of the thread on which send_message() is running
        '''
        if error is not None:
            raise error            
        self.record_members_who_received_sms(response)

    def send_message(self,receipients,message):
        '''
            send message
        '''
        sms.send(message, receipients, sender_id, callback= self.on_finish)