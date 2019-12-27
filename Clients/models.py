from datetime import date
from django.db import models
from tenant_schemas.models import TenantMixin
from tenant_schemas.utils import schema_context

from member.models import Member
from sms.models import SmsReceipients

today = date.today()
day = today.day
month = today.month
year = today.year

class Client(TenantMixin):
    #name is the name of the church
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    auto_create_schema = True

    def __str__(self):
        return self.name

    @property
    def church_code(self):
        return str(self.id).zfill(3)


class ClientDetail(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    #responsible person
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    ID_number = models.CharField(max_length=8)
    phone_number = models.CharField(max_length=15)
    #church detail.
    city_or_town = models.CharField(max_length=20)
    road_or_street = models.CharField(max_length=20)
    location_description = models.CharField(max_length=100)
    #Contact
    website = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.client)

    @property
    def on_trial(self):
        return self.client.on_trial
    @property
    def paid(self):
        return self.client.paid
    @property
    def paid_until(self):
        return self.client.paid_until
    @property
    def created_on(self):
        return self.client.created_on

    @property
    def church_code(self):
        return str(self.client.id).zfill(3)

    @property
    def number_of_members(self):
        with schema_context(self.client.schema_name):
            return Member.objects.count()

    @property
    def number_of_sms(self):
        with schema_context(self.client.schema_name):
            return SmsReceipients.objects.filter(date__month=month, date__year=year,status="Success").count()
