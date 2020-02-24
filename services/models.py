from django.db import models
from django.utils import timezone
from groups.models import ChurchGroup


class ServiceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, help_text='Name of the church service')
    description = models.CharField(max_length=150)
    church_groups = models.ManyToManyField(ChurchGroup, through='ChurchGroupMembership')
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name

class ChurchGroupMembership(models.Model):
    church_group = models.ForeignKey(ChurchGroup,on_delete=models.CASCADE, related_name='church_group_memberships')
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='church_group_memberships')

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, null=True)
    venue = models.CharField(max_length=100, help_text='The day of the service', default="none", null = True)
    date = models.DateField(help_text='The day of the service', default="2019-05-01", null = True)
    start = models.TimeField(help_text='write time e.g 00:22:19', null = True)
    end = models.TimeField(help_text='write time e.g 00:22:19', null = True)

    class Meta:
        ordering = ('-date',)

class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    action = models.CharField(max_length=100, help_text='Title of the action to be performed')
    value = models.CharField(max_length=200, help_text='The value to the title')
