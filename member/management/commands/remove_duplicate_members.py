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
                        id = contact.member.member.id
                        full_name =  contact.member.member.get_full_name()
                        if full_name not in unique_list:
                            unique_list.append(full_name)
                        else:                            
                            count += 1
                            contact.delete()
                            contact.member.member.delete()

            self.stdout.write("removed " + str(count) + " duplicates")
            self.stdout.write(str(len(duplicates)) + " duplicated phone_numbers have unique names and were not removed")
