from django.db.models import Value,F
from django.db import models

from member.models import Member

class Tag(models.Model):
    '''
        a tag to a discussion
    '''
    name = models.CharField(max_length=100)

class Discussion(models.Model):
    '''
        a discussion started in the church
    '''
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=500)
    description = models.CharField(max_length=1600)
    creation_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Member,on_delete=models.CASCADE)
    open = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, through='TagMembership',blank=True)

class TagMembership(models.Model):
    '''
        discussions belong to a tag
    '''
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

class DiscussionReaction(models.Model):
    '''
        likes towards a discussion
    '''
    REACTIONS= (
        ('L', 'Like'),
        ('R', 'Reccomend'),
        ('H', 'Heart'),
    )
    reaction = models.CharField(max_length=2, null=True, blank=True, choices=REACTIONS)
    recomendation = models.TextField(max_length=50,null=True,blank=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    reaction_by = models.ForeignKey(Member, on_delete=models.CASCADE)

class DiscussionContribution(models.Model):
    '''
        a contribution by a member towards a discussion
    '''
    discussion  =   models.ForeignKey(Discussion, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Member, on_delete=models.CASCADE)
    contribution = models.TextField(max_length=1600)
    creation_time = models.DateTimeField(auto_now_add=True)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)

class CommentToContribution(models.Model):
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

class ChannelParticipant(models.Model):
    '''
        members of a certain channel
    '''
    channel = models.ForeignKey(Channel, on_delete = models.CASCADE)
    participant = models.ForeignKey(Member, on_delete = models.CASCADE)

class ChannelMessage(models.Model):
    '''
        message in the channel
    '''
    channel = models.ForeignKey(Channel, on_delete = models.CASCADE)
    sender = models.ForeignKey(Member, on_delete = models.CASCADE)
    message = models.TextField()
    TYPE = (
        ('A', 'Announcement'),
        ('S', 'Suggestion'),
        ('Q', 'Question'),
        ('M', 'message'),
    )
    type = models.CharField(max_length=2, null=True, blank=True, choices=TYPE)
    time_stamp = models.DateTimeField(auto_now_add=True)

class PeerToPeerMessageManager(models.Manager):
    def get_queryset(self):
        qs = super(PeerToPeerMessageManager, self).get_queryset()\
            .annotate(chat_id = F('sender') + F('receiver'))
        return qs

class PeerToPeerMessage(models.Model):
    sender = models.ForeignKey(Member, on_delete = models.CASCADE, related_name="peer_to_peer_sender")
    receiver = models.ForeignKey(Member, on_delete = models.CASCADE, related_name="peer_to_peer_receiver")
    message = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = PeerToPeerMessageManager()
