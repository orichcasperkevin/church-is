from django.db import models

from groups.models import ChurchGroup
from member.models import Member


class Sms(models.Model):
    '''
        sms sent by the church are logged here
    '''
    id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=160, help_text='the app this message was sent from', default="admin")
    message = models.CharField(max_length=160, )
    sending_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='sending_member')
    receipients = models.ManyToManyField(Member, through='smsReceipients')
    church_groups = models.ManyToManyField(ChurchGroup, blank=True)
    date = models.DateField(auto_now_add=True)
    website = models.BooleanField(default=True, help_text='Publish on the website')

    class Meta:
        ordering = ('-date',)


class SmsReceipients(models.Model):
    '''
        who received the message and on what status
    '''
    sms = models.ForeignKey(Sms, on_delete=models.CASCADE)
    receipient = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='receipient')
    cost = models.CharField(max_length=20, default="0")
    status = models.CharField(max_length=10, default="0")
    date = models.DateField(auto_now_add=True)


class SmsReceipientGroups(models.Model):
    '''
        what groups will receive the message
    '''
    sms = models.ForeignKey(Sms, on_delete=models.CASCADE)
    receipient_group = models.ForeignKey(Sms, on_delete=models.CASCADE, related_name='receipient_group')
