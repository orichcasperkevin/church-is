from datetime import timedelta
from datetime import datetime

from decouple import config
from django.utils import timezone
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
    #tier info
    last_credited = models.DateField(auto_now_add=True,blank=True,null=True)

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
            today = timezone.now()
            return SmsReceipients.objects.filter(sms__date__month=today.month,status="Success").count()

    @property
    def tier(self):
        if 0 <= self.number_of_members < 500:
            return {"tier":"SM","price_per_month":999,"price_per_year":9999}

        if 500 <= self.number_of_members:
            return {"tier":"LG","price_per_month":1999,"price_per_year":19999}



    @property
    def apprx_number_of_days_left(self):
        price_per_month = self.tier['price_per_month']
        price_per_day = (price_per_month / 30)
        return int(float(self.credit) / price_per_day)

    @property
    def sms_credentials(self):
        return ChurchSMSCredentials.objects.get_or_create(church_id=self.client.id)[0]

    @property
    def domain_url(self):
        return self.client.domain_url
'''
    client sms service
'''

class ChurchSMSCredentials(models.Model):
    church = models.OneToOneField(Client,on_delete=models.CASCADE)
    at_username =  models.CharField(max_length=50,default=config('DEMO_AFRICAS_TALKING_USERNAME'))
    at_api_key = models.CharField(max_length=150,default=config('DEMO_AFRICAS_TALKING_API_KEY'))
    at_mpesa_acc_no = models.CharField(max_length=50,default="demo.api",null=True,blank=True)
    at_mpesa_paybill = models.CharField(max_length=20,default="525900",null=True,blank=True)

'''
    the following is used as website content for thhe client church
'''
class ChurchLogo(models.Model):
    church = models.OneToOneField(Client,on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='images/')

class ChurchAbout(models.Model):
    church = models.OneToOneField(Client,on_delete=models.CASCADE)
    about = models.TextField(max_length=500)

class ChurchStatement(models.Model):
    church = models.OneToOneField(Client,on_delete=models.CASCADE)
    mission = models.TextField(max_length=150)
    vision = models.TextField(max_length=150)

class ChurchCoreValue(models.Model):
    church = models.ForeignKey(Client,on_delete=models.CASCADE)
    value = models.TextField(max_length=20)

class ChurchPeriodicTheme(models.Model):
    church = models.ForeignKey(Client,on_delete=models.CASCADE)
    theme = models.TextField(max_length=150)
    description = models.TextField(max_length=500)
    start = models.DateField()
    end = models.DateField()

    class Meta:
        ordering = ('-start',)
