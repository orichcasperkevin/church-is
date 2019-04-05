from django.db import models

# Create your models here.
from groups.models import ChurchGroup
from member.models import Member


class Duty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Duties'

    def __str__(self):
        return self.name


class DutyRoster(models.Model):
    '''
        Duty roaster assigns duties to members in given period
        of time in a given church
    '''
    members = models.ManyToManyField(Member,blank = True)
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.member)

    class Meta:
        verbose_name_plural = 'Roster'
        verbose_name = 'Roster'