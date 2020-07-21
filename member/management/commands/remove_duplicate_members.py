from django.core.management.base import BaseCommand
from django.db.models import Count
from tenant_schemas.utils import schema_context

from django.contrib.auth.models import User
from Clients.models import Client
from member.models import Member,MemberContact

class Command(BaseCommand):
    help = 'Remove duplicate members'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Select client ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        client = Client.objects.get(id=id)
        self.stdout.write("remove duplicates for schema --->" + str(client.schema_name))
        print("\n")

        with schema_context(client.schema_name):
            count = 0
            duplicates = MemberContact.objects.values('phone')\
                        .annotate(count=Count('phone')).filter(count__gt=1)
            for duplicate in duplicates:
                contacts = MemberContact.objects.filter(phone = duplicate['phone'])
                unique_list = []
                for contact in contacts:
                    if contact.member:
                        phone = contact.phone
                        # full_name =  contact.member.member.get_full_name()
                        if phone not in unique_list:
                            print(phone)
                            unique_list.append(phone)
                        else:
                            print(phone + "---> phone number duplicated ")
                            count += 1
                            contact.delete()
                            contact.member.member.delete()
                print("\n")

            self.stdout.write("removed " + str(count) + " duplicates")            
