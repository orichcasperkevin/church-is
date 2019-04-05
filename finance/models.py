from django.db import models

from groups.models import ChurchGroup
from member.models import Member
from projects.models import Project, Pledge


# Create your models here.


class Offering(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(help_text='The Date of the offering collection')
    church_group = models.ManyToManyField(ChurchGroup)
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='offering_recorded_by')

    def __str__(self):
        return 'offering of Ksh.' + str(self.amount) + ' on ' + str(self.date)


class TitheParent(models.Model):
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='tithe_recorded_by')

    def __str__(self):
        return 'member tithe'

    class Meta:
        verbose_name_plural = 'Member Tithes'
        verbose_name = 'Member Tithe'


class Tithe(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    narration = models.TextField(blank=True)
    parent = models.ForeignKey(TitheParent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.member) + ' tithe of ' + str(self.amount)


class Contribution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='contribution_recorded_by')

    def __str__(self):
        return str(self.amount) + ' contribution for ' + str(self.project)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.project.raised_amount = self.project.raised_amount + self.amount
        self.project.save()
        super(Contribution, self).save(force_insert=False, force_update=False, using=None,
                                       update_fields=None)


class IncomeType(models.Model):
    type_name = models.CharField(max_length=100,
                                 help_text='Other type of income apart from tithes,offertory or contribution')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type_name


class Income(models.Model):
    type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='income_recorded_by')

    def __str__(self):
        return str(self.type) + ' ' + str(self.amount)


class ExpenditureType(models.Model):
    type_name = models.CharField(max_length=100,
                                 help_text='Type of church expenditure')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type_name


class Expenditure(models.Model):
    type = models.ForeignKey(ExpenditureType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='expenditure_recorded_by')

    def __str__(self):
        return str(self.type) + ' ' + str(self.amount)


class PledgePayment(Pledge):
    class Meta:
        proxy = True
