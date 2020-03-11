from django.db import models
from church_social.models import  Channel,ChannelParticipant
from member.models import Member, Role


class GroupOfChurchGroups(models.Model):
    '''
        a group of church groups
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    @property
    def number_of_groups(self):
        return ChurchGroup.objects.filter(group_id = self.id).count() or 0

class ChurchGroupModelManager(models.Manager):
    '''
        we need to create a channel every time a group is created
    '''
    def create(self,**obj_data):
        group_name  = (obj_data['name'])
        description = (obj_data['description'])
        channel_name = ('_').join(group_name.split(' '))

        #create the channel for this group
        Channel.objects.create(name=channel_name,description=description,open=True)
        return super().create(**obj_data)

class ChurchGroup(models.Model):
    '''
        the name and description of the group
    '''
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(GroupOfChurchGroups, null = True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50,blank=True)
    group_members = models.ManyToManyField(Member, through='ChurchGroupMembership', blank=True)
    anvil_space_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def number_of_members(self):
        return self.group_members.all().count() or 0

    objects = ChurchGroupModelManager()

class ChurchGroupMembershipModelManager(models.Manager):
    '''
        because we need to create add a member to a channel whenever they are added to a group
    '''
    def create(self,**obj_data):
        member  = (obj_data['member'])
        church_group = (obj_data['church_group'])
        church_group_name = church_group.name
        channel = Channel.objects.get(name=('_').join(church_group_name.split(' ')))
        #create ChannelParticipant
        ChannelParticipant.objects.create(channel_id=channel.id,participant_id=member.id)
        return super().create(**obj_data)

class ChurchGroupMembership(models.Model):
    '''
        members of a church group
    '''
    id = models.AutoField(primary_key=True)
    church_group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    objects = ChurchGroupMembershipModelManager()
