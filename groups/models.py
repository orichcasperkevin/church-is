from django.db import models

from member.models import Member, Role

class GroupOfChurchGroups(models.Model):
    '''
        a group of church groups
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)

class ChurchGroup(models.Model):
    '''
        the name and description of the group
    '''
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(GroupOfChurchGroups, null = True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    group_members = models.ManyToManyField(Member, through='ChurchGroupMembership', blank=True)

    def number_of_members(self):
        number = 0
        for data in self.group_members.all():
            number = number + 1
        return number


class ChurchGroupMembership(models.Model):
    '''
        members of a church group
    '''
    id = models.AutoField(primary_key=True)
    church_group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)


class GroupMeeting(models.Model):
    '''
        a group meeting as hosted by a member, at a location on a certain date
    '''
    group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)
    host = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='group_meeting_host',
                             help_text='Names of the host being visited.', blank=True)
    location = models.CharField(max_length=20, help_text='The location of the meeting')
    date = models.DateField(help_text='The visit date')
    attendees = models.ManyToManyField(Member, through='GroupMeetingRoster')

    @property
    def number_of_attendees(self):
        number = 0
        for data in self.attendees.all():
            number = number + 1
        return number


class GroupMeetingRoster(models.Model):
    '''
        a member that attended the group meeting
    '''
    group_meeting = models.ForeignKey(GroupMeeting, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Member, on_delete=models.CASCADE)


class GroupPhoto(models.Model):
    '''
        the photos of grouped under a group,
        can be tagged as belonging to a certain fellowship meeting that the attended
        can also be tagged as belonging or containing a certain member or members
    '''
    group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)
    group_meeting = models.ForeignKey(GroupMeeting, on_delete=models.CASCADE, null=True, blank=True)
    group_meeting_attendees = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True)
    photo = models.ImageField(upload_to='fellowships/', null=True)
