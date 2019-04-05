from django.db import models

from groups.models import ChurchGroup


class Service(models.Model):
    church_group = models.ManyToManyField(ChurchGroup, help_text='The church groups this service is intended for.')
    name = models.CharField(max_length=150, help_text='Name of the church service')
    date = models.DateField(help_text='The day of the service')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ('-date',)


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    action = models.CharField(max_length=100, help_text='Title of the action to be performed')
    value = models.CharField(max_length=200, help_text='The value to the title')
    start = models.TimeField(help_text='write time e.g 00:22:19')
    end = models.TimeField(help_text='write time e.g 00:22:19')

    def __str__(self):
        return str(self.action) + ': ' + str(self.value)
