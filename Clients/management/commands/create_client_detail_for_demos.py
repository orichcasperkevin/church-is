from django.core.management.base import BaseCommand, CommandError
from Clients.models import Client,ClientDetail

class Command(BaseCommand):
    help = 'created to solve the issue of demos not having client details'


    def handle(self, *args, **options):
        for client in Client.objects.filter(on_trial=True):
            ClientDetail.objects.create(client=client,
                            first_name="demo first name",
                            last_name="demo last name",
                            phone_number="07#########",
                            credit=0.00)
        print("\n" + "......done......")
