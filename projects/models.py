from decimal import Decimal

from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum,Avg
from django.template.defaultfilters import floatformat

from groups.models import ChurchGroup
from member.models import Member


# Create your models here.

class Project(models.Model):
    """Church undertaking project"""
    id = models.AutoField(primary_key=True)
    church_group = models.ManyToManyField(ChurchGroup, blank=True)
    name = models.CharField(max_length=100, help_text='The name of the project')
    start = models.DateField(verbose_name='Starting Date', help_text='Start date of the project')
    stop = models.DateField(verbose_name='Completion Date', help_text='Completion date of the project')
    description = models.TextField(help_text='Description of the project')
    required_amount = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))

    def __str__(self):
        return self.name
        
    @property
    def raised_amount(self):
        '''
          This is cumulatively added when members bring in contributions or
          service their pledges.
        '''
        pledge_payment = PledgePayment.objects.filter(pledge__project__id=self.id).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0
        contributions = Contribution.objects.filter(project_id=self.id).aggregate(Sum('amount'))['amount__sum'] or 0

        return pledge_payment + contributions

    @property
    def total_in_pledges(self):
        '''
            the total amount that has been pledged so far.
        '''
        return Pledge.objects.filter(project_id=self.id).aggregate(Sum('amount'))['amount__sum'] or 0

    @property
    def total_in_settled_pledges(self):
        '''
            the total amount that has been settled in pledges
        '''
        return  PledgePayment.objects.filter(pledge__project__id=self.id).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0

    @property
    def percentage_of_pledge_settled(self):
        '''
            the percentage of pledges that has been funded so far.
        '''
        if (self.total_in_pledges == 0):
            percent = 0
        else:
            percent = (self.total_in_settled_pledges / self.total_in_pledges) * 100

        percent = floatformat(percent, 2)
        return percent

    @property
    def remaining_amount(self):
        '''
            the amount remaining before the project if fully funded
        '''
        return intcomma(self.required_amount - self.raised_amount)

    @property
    def percentage_funded(self):
        '''
            the percentage that has been funded so far.
        '''
        percent = (self.raised_amount / self.required_amount) * 100
        percent = floatformat(percent, 2)
        return percent


class Contribution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects')
    anonymous = models.BooleanField(default=False)
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE, related_name='members')
    names = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL,
                                    related_name='contribution_recorded_bys')
    recorded_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-recorded_at',)



class Pledge(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE)
    names = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    date = models.DateField(verbose_name='Pledge Payment Date')
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='pledge_recorded_by')
    recorded_at = models.DateTimeField(auto_now_add=True)

    @property
    def amount_so_far(self):
        return  PledgePayment.objects.filter(pledge_id=self.id).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0

    @property
    def remaining_amount(self):
        return self.amount - self.amount_so_far

    @property
    def percentage_funded(self):
        percent = (self.amount_so_far / self.amount) * 100
        percent = floatformat(percent, 2)
        return str(percent) + '%'


class PledgePayment(models.Model):
    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    payment_recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL,
                                            related_name='payment_recorded_by')
    payment_recorded_on = models.DateTimeField(auto_now_add=True)


class PendingConfirmation(models.Model):
    '''
        pending payment confirmations
    '''
    confirming_for = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True, related_name='confirming_for')
    for_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='for_projects',null=True)
    TYPE = (
            ('C', 'Contribution'),
            ('P', 'PledgeSettlement'),
    )
    confirmation_message = models.TextField(max_length=500)
    type = models.CharField(max_length=2, null=True, blank=True, choices=TYPE)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)

    def confirmPayment(self):
        '''
            confirm that the payment has been made
        '''
        #TODO tun this offering to queryset without doing a filter
        if (self.type == "C"):
            contribution =  Contribution.objects.create(project=self.for_project,member=self.confirming_for,amount=self.amount)
            self.delete()
            return Contribution.objects.filter(id=contribution.id)
        else:
            pledge = Pledge.objects.get(project_id = self.for_project.id,member__member__id = self.confirming_for.member.id)
            payment =  PledgePayment.objects.create(pledge=pledge,payment_amount=self.amount)
            self.delete()
            return PledgePayment.objects.filter(id=payment.id)
