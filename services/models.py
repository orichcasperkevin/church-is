from django.db import models

from groups.models import ChurchGroup


class Service(models.Model):
    name = models.CharField(max_length=150, help_text='Name of the church service')
    church_groups = models.ManyToManyField(ChurchGroup, through='ChurchGroupMembership')

class ChurchGroupMembership(models.Model):
    church_group = models.ForeignKey(ChurchGroup,on_delete=models.CASCADE, related_name='church_group_memberships')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='church_group_memberships') 

class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    action = models.CharField(max_length=100, help_text='Title of the action to be performed')
    value = models.CharField(max_length=200, help_text='The value to the title')
    venue = models.CharField(max_length=100, help_text='The day of the service', default="none")
    date = models.DateField(help_text='The day of the service', default="2019-05-01")
    start = models.TimeField(help_text='write time e.g 00:22:19')
    end = models.TimeField(help_text='write time e.g 00:22:19')

    class Meta:
        ordering = ('-date',)
