from django.core.management.base import BaseCommand

from Clients.models import Client

class Command(BaseCommand):
    help = 'Checks the client detail for the given ID'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Select client ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        client = Client.objects.get(id=id)
        self.stdout.write(str(client.__dict__))
