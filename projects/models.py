from decimal import Decimal

from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import floatformat

from groups.models import ChurchGroup
from member.models import Member


# Create your models here.


class Project(models.Model):
    """Church undertaking project"""
    id = models.AutoField(primary_key = True)
    church_group = models.ManyToManyField(ChurchGroup, help_text='The church groups this project belongs to.')
    name = models.CharField(max_length=100, help_text='The name of the project')
    start = models.DateField(verbose_name='Starting Date', help_text='Start date of the project')
    stop = models.DateField(verbose_name='Completion Date', help_text='Completion date of the project')
    description = models.TextField(help_text='Description of the project')
    required_amount = models.DecimalField(max_digits=15, decimal_places=2,
                                          validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    @property
    def raised_amount(self):
        '''
          This is cumulatively added when members bring in contributions or
          service their pledges.
        '''
        project_id = self.id
        queryset = PledgePayment.objects.filter(pledge__project__id=project_id)
        raised_amount = 0
        for payment in queryset:
            raised_amount += payment.payment_amount

        queryset = Contribution.objects.filter(project_id=project_id)
        for contribution in queryset:
            raised_amount += contribution.amount
        return raised_amount

    @property
    def remaining_amount(self):
        return intcomma(self.required_amount - self.raised_amount)

    @property
    def percentage_funded(self):
        percent = (self.raised_amount / self.required_amount) * 100
        percent = floatformat(percent, 2)
        return percent

class Contribution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='projects')
    anonymous = models.BooleanField(default=False)
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE,related_name='members')
    names = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15,blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='contribution_recorded_bys')
    recorded_at = models.DateTimeField(auto_now_add=True)

class Pledge(models.Model):
    id = models.AutoField(primary_key = True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE)
    names = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15,blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    date = models.DateField(verbose_name='Pledge Payment Date')
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='pledge_recorded_by')
    recorded_at = models.DateTimeField(auto_now_add=True)

    @property
    def amount_so_far(self):
         queryset = PledgePayment.objects.filter(pledge_id=self.id)
         amount_so_far = 0
         for pledge_payment in queryset:
            amount_so_far += pledge_payment.payment_amount
         return amount_so_far

    @property
    def remaining_amount(self):
        return intcomma(self.amount - self.amount_so_far)

    @property
    def percentage_funded(self):
        percent = (self.amount_so_far / self.amount) * 100
        percent = floatformat(percent, 2)
        return str(percent) + '%'

class PledgePayment(models.Model):
    pledge = models.ForeignKey(Pledge,on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    payment_recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='payment_recorded_by')
    payment_recorded_on = models.DateTimeField(auto_now_add=True)
    
