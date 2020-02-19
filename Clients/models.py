from datetime import datetime
from django.db import models
from tenant_schemas.models import TenantMixin
from tenant_schemas.utils import schema_context

from member.models import Member
from sms.models import SmsReceipients

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
    ID_number = models.CharField(max_length=8,default="demo")
    phone_number = models.CharField(max_length=15,default="demo")
    #church detail.
    city_or_town = models.CharField(max_length=20,default="demo")
    road_or_street = models.CharField(max_length=20,default="demo")
    location_description = models.CharField(max_length=100,default="demo")
    #Contact
    website = models.CharField(max_length=50,null=True,blank=True,default="demo")
    #amount of credit remaining
    credit = models.DecimalField(max_digits=15, decimal_places=2,default=0.00,null=True,blank=True)
    last_credited = models.DateTimeField(default=datetime.now(), blank=True)
    #sms quota remaining
    sms_quota = models.IntegerField(default=0,null=True,blank=True)

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
            return SmsReceipients.objects.filter(sms__date__gt=self.last_credited,status="Success").count()

    @property
    def tier(self):
        if 0 <= self.number_of_members < 250:
            return {"tier":"XSM","price_per_month":1500,"price_per_year":15000}
        if 250 <= self.number_of_members < 500:
            return {"tier":"SM","price_per_month":3000,"price_per_year":30000}
        if 500 <= self.number_of_members < 750:
            return {"tier":"MD","price_per_month":4500,"price_per_year":45000}
        if 750 <= self.number_of_members < 100:
            return {"tier":"LG","price_per_month":6000,"price_per_year":60000}
        if 1000 <= self.number_of_members:
            return {"tier":"XLG","price_per_month":7500,"price_per_year":75000}

    @property
    def apprx_number_of_days_left(self):
        price_per_month = self.tier['price_per_month']
        price_per_day = (price_per_month / 30)
        return int(float(self.credit) / price_per_day)
