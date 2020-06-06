# Create your models here.
from datetime import date

from django.db import models
from django.db.models import Sum
from django.utils.timezone import now

from groups.models import ChurchGroup
from services.models import Service
from member.models import Member

today = date.today()
day = today.day
month = today.month
year = today.year

class PendingConfirmation(models.Model):
    confirming_for = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    TYPE = (
            ('O', 'Offering'),
            ('T', 'Tithe'),
    )
    confirmation_message = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=2, null=True, blank=True, choices=TYPE)
    amount = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)

    def confirmPayment(self):
        '''
            confirm that the payment has been made
        '''
        #TODO tun this offering to queryset without doing a filter
        if (self.type == "O"):
            offering =  Offering.objects.create(member=self.confirming_for,amount=self.amount,date=now().date())
            self.delete()
            return Offering.objects.filter(id=offering.id)
        else:
            tithe =  Tithe.objects.create(member=self.confirming_for,amount=self.amount)
            self.delete()
            return Tithe.objects.filter(id=tithe.id)

class ModeOfPayment(models.Model):
    name = models.CharField(max_length=50)

class OfferingType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=160,blank=True,null=True)

    def __str__(self):
        return self.name

class Offering(models.Model):
    type = models.ForeignKey(OfferingType, on_delete=models.CASCADE, null=True, blank=True)
    mode_of_payment = models.ForeignKey(ModeOfPayment,on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    #by who or what
    name_if_not_member = models.CharField(max_length=20, blank=True, null=True)
    phone_if_not_memmber = models.CharField(max_length=20,blank=True,null=True)
    group = models.ForeignKey(ChurchGroup,on_delete=models.CASCADE, blank=True, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    # the service this offering was collected from
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='offering_recorded_by')

    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def total_this_month(self):
        if self.member:
            sum = Offering.objects.filter(member_id=self.member.id, date__month=month, date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0
        if self.group:
            sum = Offering.objects.filter(group_id=self.group.id, date__month=month, date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0
        if self.service:
            sum = Offering.objects.filter(service_id=self.service.id, date__month=month, date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0

    @property
    def total_this_year(self):
        if self.member:
            sum = Offering.objects.filter(member_id=self.member.id, date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0
        if self.group:
            sum = Offering.objects.filter(group_id=self.group.id,date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0
        if self.service:
            sum = Offering.objects.filter(service_id=self.service.id,date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0

class Tithe(models.Model):
    '''
        tithe collected for a member
    '''
    mode_of_payment = models.ForeignKey(ModeOfPayment,on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    #by who or what
    name_if_not_member = models.CharField(max_length=20, blank=True, null=True)
    phone_if_not_memmber = models.CharField(max_length=20,blank=True,null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(ChurchGroup,on_delete=models.CASCADE, blank=True, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE,null=True,blank=True)
    #when
    date = models.DateField()
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='tithe_recorded_by')

    timestamp = models.DateTimeField(auto_now_add=True,null=True)

    @property
    def total_this_month(self):
        if self.member:
            sum = Tithe.objects.filter(member_id=self.member.id, date__month=month, date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0
        if self.group:
            sum = Tithe.objects.filter(group_id=self.group.id, date__month=month, date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0
        if self.service:
            sum = Tithe.objects.filter(service_id=self.service.id, date__month=month, date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0

    @property
    def total_this_year(self):
        if self.member:
            sum = Tithe.objects.filter(member_id=self.member.id, date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0
        if self.group:
            sum = Tithe.objects.filter(group_id=self.group.id,date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0
        if self.service:
            sum = Tithe.objects.filter(service_id=self.service.id,date__year=year)\
                            .aggregate(Sum('amount'))
            return sum['amount__sum'] or 0

class IncomeType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type_name

    @property
    def total_this_month(self):
        sum = Income.objects.filter(type_id=self.id, date__month=month, date__year=year).aggregate(Sum('amount'))
        return sum['amount__sum'] or 0

    @property
    def total_this_year(self):
        sum = Income.objects.filter(type_id=self.id, date__year=year).aggregate(Sum('amount'))
        return sum['amount__sum'] or 0

class Income(models.Model):
    type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    mode_of_payment = models.ForeignKey(ModeOfPayment,on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='income_recorded_by')

    @property
    def total_overall_income_this_month(self):
        sum = Income.objects.filter(date__month=month, date__year=year).aggregate(Sum('amount'))
        return sum['amount__sum']

    @property
    def total_overall_income_this_year(self):
        sum = Income.objects.filter(date__year=year).aggregate(Sum('amount'))
        return sum['amount__sum'] or 0

class ExpenditureType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type_name

    @property
    def total_this_month(self):
        sum = Expenditure.objects.filter(type_id=self.id,date__month=month, date__year=year).aggregate(Sum('amount'))
        return sum['amount__sum'] or 0

    @property
    def total_this_year(self):
        sum = Expenditure.objects.filter(type_id=self.id,date__year=year).aggregate(Sum('amount'))
        return sum['amount__sum'] or 0

class Expenditure(models.Model):
    type = models.ForeignKey(ExpenditureType, on_delete=models.CASCADE)
    mode_of_payment = models.ForeignKey(ModeOfPayment,on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL,
                                    related_name='expenditure_recorded_by')

class CSV(models.Model):
    '''
        csv for importing finace data
    '''
    csv = models.FileField(upload_to='Resources/',null=True)
