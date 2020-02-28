import schedule
import time

from django.core.management.base import BaseCommand, CommandError
from Clients.models import ClientDetail

PRICE_PER_MONTH = 5000

class Command(BaseCommand):
    help = 'starts the job that updates client credits every midnight'


    def handle(self, *args, **options):
        self.scheduleJobs()

    def job(self):
        for client_detail in ClientDetail.objects.all():
            initial_credit = client_detail.credit
            price_per_month = client_detail.tier['price_per_month']
            final_credit = float(initial_credit) - (price_per_month / 30)
            if final_credit <= 0:# dont allow final_credit to go below zero
                final_credit = 0
            client_detail.credit = final_credit
            client_detail.save()

    def scheduleJobs(self):
        schedule.every().day.at("00:00").do(self.job)
        #logging
        self.stdout.write(self.style.SUCCESS('job successfully started.'))
        self.stdout.write('...CTRL + Z then type  `bg` to push to the background...')
        self.stdout.write('\n')
        self.stdout.write('`jobs` to check on the process and `kill%<job id>` to kill it')

        while True:
            schedule.run_pending()
            time.sleep(1)
