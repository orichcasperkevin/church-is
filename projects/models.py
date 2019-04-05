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
    church_group = models.ManyToManyField(ChurchGroup, help_text='The church groups this project belongs to.')
    name = models.CharField(max_length=100, help_text='The name of the project')
    start = models.DateField(verbose_name='Starting Date', help_text='Start date of the project')
    stop = models.DateField(verbose_name='Completion Date', help_text='Completion date of the project')
    description = models.TextField(help_text='Description of the project')
    required_amount = models.DecimalField(max_digits=15, decimal_places=2,
                                          validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    raised_amount = models.DecimalField(max_digits=15, decimal_places=2,
                                        help_text='This is cumulatively added when members bring in contributions or '
                                                  'contribution from another place, e.g a fundraising',
                                        validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))

    def __str__(self):
        return str(self.name)

    @property
    def remaining_amount(self):
        return intcomma(self.required_amount - self.raised_amount)

    @property
    def percentage_funded(self):
        percent = (self.raised_amount / self.required_amount) * 100
        percent = floatformat(percent, 2)
        return str(percent) + '%'


class Pledge(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE,
                               help_text='If the person pledging is church member,Select them from the '
                                         'list,If not record their names. '
                                         'You can\'t record a name and also have a member.Record only one.')
    names = models.CharField(max_length=100, blank=True,
                             help_text='If the person pledging is not a church member, record their names.'
                                       ' You can\'t record a name and also have a member.Record only one.')
    phone = models.CharField(max_length=15,
                             help_text='If the person pledging is not a member, record their phone number',
                             blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    date = models.DateField(verbose_name='Pledge Payment Date')
    details = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='pledge_recorded_by')
    recorded_at = models.DateTimeField(auto_now_add=True)
    payed_on = models.DateField(null=True)
    payed_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    payed = models.BooleanField(default=False, verbose_name='payment complete')
    payment_recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='payment_by')
    narration = models.TextField(blank=True)