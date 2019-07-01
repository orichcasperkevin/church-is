# Create your models here.
from datetime import date

from django.db import models

from groups.models import ChurchGroup
from member.models import Member

today = date.today()
day = today.day
month = today.month
year = today.year


class Offering(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(help_text='The Date of the offering collection')
    anonymous = models.BooleanField(default=False)
    name_if_not_member = models.CharField(max_length=50, blank=True, null=True)
    church_group = models.ManyToManyField(ChurchGroup, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='offering_recorded_by')

    @property
    def total_this_month(self):
        total = 0.00
        for data in Offering.objects.filter(member_id=self.member_id, date__month=month, date__year=year):
            total = total + float(data.amount)
        return total

    @property
    def total_this_year(self):
        total = 0.00
        for data in Offering.objects.filter(member_id=self.member_id, date__year=year):
            total = total + float(data.amount)
        return total


class GroupOffering(models.Model):
    offering = models.ForeignKey(Offering, on_delete=models.CASCADE)
    church_group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)


class Tithe(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='tithe_recorded_by')

    @property
    def total_this_month(self):
        total = 0.00
        for data in Tithe.objects.filter(member_id=self.member_id, date__month=month, date__year=year):
            total = total + float(data.amount)
        return total

    @property
    def total_this_year(self):
        total = 0.00
        for data in Tithe.objects.filter(member_id=self.member_id, date__year=year):
            total = total + float(data.amount)
        return total


class IncomeType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100,
                                 help_text='Other type of income apart from tithes,offertory or contribution')
    description = models.TextField(blank=True)

    @property
    def total_this_month(self):
        total = 0
        for data in Income.objects.filter(type_id=self.id, date__month=month, date__year=year):
            total = total + data.amount
        return total

    @property
    def total_this_year(self):
        total = 0
        for data in Income.objects.filter(type_id=self.id, date__year=year):
            total = total + data.amount
        return total


class Income(models.Model):
    type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='income_recorded_by')

    @property
    def total_overall_income_this_month(self):
        total = 0
        for data in Income.objects.filter(date__month=month, date__year=year):
            total = total + data.amount
        return total

    @property
    def total_overall_income_this_year(self):
        total = 0
        for data in Income.objects.filter(date__year=year):
            total = total + data.amount
        return total


class ExpenditureType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100,
                                 help_text='Type of church expenditure')
    description = models.TextField(blank=True)

    @property
    def total_this_month(self):
        total = 0
        for data in Expenditure.objects.filter(type_id=self.id, date__month=month, date__year=year):
            total = total + data.amount
        return total

    @property
    def total_this_year(self):
        total = 0
        for data in Expenditure.objects.filter(type_id=self.id, date__year=year):
            total = total + data.amount
        return total


class Expenditure(models.Model):
    type = models.ForeignKey(ExpenditureType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    narration = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL,
                                    related_name='expenditure_recorded_by')

    @property
    def total_overall_expenditure_this_month(self):
        total = 0
        for data in Expenditure.objects.filter(date__month=month, date__year=year):
            total = total + data.amount
        return total

    @property
    def total_overall_expenditure_this_year(self):
        total = 0
        for data in Expenditure.objects.filter(date__year=year):
            total = total + data.amount
        return total
