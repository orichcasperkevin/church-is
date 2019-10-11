from django.db import models

from member.models import Member
from groups.models import ChurchGroup

class Discussion(models.Model):
    '''
        a discussion started in the church
    '''
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    creation_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Member,on_delete=models.CASCADE)
    open = models.BooleanField(default=True)

class DiscussionContribution(models.Model):
    '''
        a contribution by a member towards a discussion
    '''
    discussion  =   models.ForeignKey(Discussion, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Member, on_delete=models.CASCADE)
    contribution = models.TextField(max_length=160)
    creation_time = models.DateTimeField(auto_now_add=True)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)

class commentToContribution(models.Model):
    '''
        a comment toward a contribution
    '''
    contribution = models.ForeignKey(DiscussionContribution, on_delete=models.CASCADE)
    comment = models.TextField(max_length=160)
    commentor = models.ForeignKey(Member, on_delete = models.CASCADE)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)

class Channel(models.Model):
    '''
        a temporal or permanent communication channel ,
        messages in a channel will reach everyone in the channel's sms inbox
        they can chat and make arrangements on this channel.
    '''
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    open = models.BooleanField(default=False)
    live = models.BooleanField(default = False)

class ChannelMessage(models.Model):
    '''
        message in the channel
    '''
    channel = models.ForeignKey(Channel, on_delete = models.CASCADE)
    sender = models.ForeignKey(Member, on_delete = models.CASCADE)
    important = models.BooleanField(default=False)
    message = models.TextField(max_length=160)
    creation_time = models.DateTimeField(auto_now_add=True)
