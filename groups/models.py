from django.db import models
from member.models import Member,Role

from datetime import date

# Create your models here.
class Fellowship(models.Model):
    '''
        the name and description of the fellowship
    '''
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    fellowship_members = models.ManyToManyField(Member, through = 'FellowshipMembership', blank = True)

    @property
    def number_of_members(self):
        number = 0
        for data in self.fellowship_members.all():
            number = number + 1
        return number

    def __str__(self):
        return self.name

class FellowshipMembership(models.Model):
    '''
        members of a fellowship
    '''
    id = models.AutoField(primary_key = True)
    fellowship = models.ForeignKey(Fellowship,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)



class FellowshipMeeting(models.Model):
    '''
        a fellowship as hosted by a member, at a location on a certain date
    '''
    fellowship = models.ForeignKey(Fellowship, on_delete=models.CASCADE)
    host = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='hosts', help_text='Names of the host being visited.')
    location = models.CharField(max_length=200, help_text='The location of the host')
    date = models.DateField(help_text='The visit date')
    attendees = models.ManyToManyField(Member, through = 'FellowshipMeetingRoster')

    @property
    def number_of_attendees(self):
        number = 0
        for data in self.attendees.all():
            number = number + 1
        return number


class FellowshipMeetingRoster(models.Model):
    '''
        a member that attended the fellowship in the fellowshipRoster
    '''
    fellowship_meeting = models.ForeignKey(FellowshipMeeting, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Member,blank = True,on_delete=models.CASCADE)



class FellowshipPhoto(models.Model):
    '''
        the photos of grouped under a fellowship,
        can be tagged as belonging to a certain fellowship meeting that the attended
        can also be tagged as belonging or containing a certain member or members
    '''
    fellowship = models.ForeignKey(Fellowship, on_delete=models.CASCADE)
    fellowship_meeting = models.ForeignKey(FellowshipMeeting,on_delete=models.CASCADE,null=True,blank=True)
    photo = models.ImageField(upload_to='fellowships/', null=True)



class CellGroup(models.Model):
    '''
        cell group
    '''
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cell_group_members = models.ManyToManyField(Member,through = 'CellGroupMembership',related_name='cell_group_members',blank = True)

    def number_of_members(self):
        number = 0
        for data in self.cell_group_members.all():
            number = number + 1
        return number

    def __str__(self):
        return self.name

class CellGroupMembership(models.Model):
    '''
        members of a cell group
    '''
    id = models.AutoField(primary_key = True)
    cell_group = models.ForeignKey(CellGroup,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)



class CellGroupMeeting(models.Model):
    '''
        a cell group as hosted by a member on a date
    '''
    id = models.AutoField(primary_key = True)
    cell_group = models.ForeignKey(CellGroup, on_delete=models.CASCADE)
    host = models.ForeignKey(Member, on_delete = models.CASCADE,related_name="cell_group_host", help_text='Names of the host being visited.',)
    location = models.CharField(max_length=200, help_text='The location of the host')
    date = models.DateField(help_text='The visit date')
    attendees = models.ManyToManyField(Member, through='CellGroupMeetingRoster')

    @property
    def number_of_attendees(self):
        number = 0
        for data in self.attendees.all():
            number = number + 1
        return number

class CellGroupMeetingRoster(models.Model):
    '''
        a member that attended the cellGroup in the cellGroupRoster
    '''
    id = models.AutoField(primary_key = True)
    cell_group_meeting = models.ForeignKey(CellGroupMeeting, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Member,blank = True,on_delete=models.CASCADE)



class CellGroupPhoto(models.Model):
    '''
        the photos grouped under a cell group,
        can be tagged as belonging to a certain cellGroup meeting that was attended
        can also be tagged as belonging or containing a certain member or members
    '''
    cell_group = models.ForeignKey(CellGroup, on_delete=models.CASCADE)
    cell_group_meeting = models.ForeignKey(CellGroupMeeting,on_delete=models.CASCADE,null=True,blank=True)
    photo = models.ImageField(upload_to='cell_groups/',)


class ChurchGroup(models.Model):
    '''
        the name and description of the group
    '''
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    group_members = models.ManyToManyField(Member, through = 'ChurchGroupMembership',blank = True)

    def number_of_members(self):
        number = 0
        for data in self.group_members.all():
            number = number + 1
        return number


class ChurchGroupMembership(models.Model):
    '''
        members of a church group
    '''
    id = models.AutoField(primary_key = True)
    church_group = models.ForeignKey(ChurchGroup,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)


class GroupMeeting(models.Model):
    '''
        a group meeting as hosted by a member, at a location on a certain date
    '''
    group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)
    host = models.ForeignKey(Member,on_delete=models.CASCADE, related_name = 'group_meeting_host', help_text='Names of the host being visited.',blank =True)
    location = models.CharField(max_length=200, help_text='The location of the meeting')
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
    attendee = models.ForeignKey(Member,on_delete=models.CASCADE)



class GroupPhoto(models.Model):
    '''
        the photos of grouped under a group,
        can be tagged as belonging to a certain fellowship meeting that the attended
        can also be tagged as belonging or containing a certain member or members
    '''
    group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)
    group_meeting = models.ForeignKey(GroupMeeting,on_delete=models.CASCADE,null=True,blank=True)
    group_meeting_attendees = models.ForeignKey(Member, on_delete = models.CASCADE ,blank=True)
    photo = models.ImageField(upload_to='fellowships/', null=True)


class Ministry(models.Model):
    '''
        the name and description of the group
    '''
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(Member, through = "MinistryMembership",blank = True)

    def number_of_members(self):
        number = 0
        for data in self.members.all():
            number = number + 1
        return number

    def __str__(self):
        return self.name


class MinistryMembership(models.Model):
    '''
        members of a Ministry
    '''
    id = models.AutoField(primary_key = True)
    ministry = models.ForeignKey(Ministry,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)


class MinistryMeeting(models.Model):
    '''
        a ministry meeting as hosted by a member, at a location on a certain date
    '''
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    host = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='ministry_meeting_host', help_text='Names of the host being visited.',blank =True)
    location = models.CharField(max_length=200, help_text='The location of the meeting')
    date = models.DateField(help_text='The visit date')
    attendees = models.ManyToManyField(Member,through='MinistryMeetingRoster')

    @property
    def number_of_attendees(self):
        number = 0
        for data in self.attendees.all():
            number = number + 1
        return number

class MinistryMeetingRoster(models.Model):
    '''
        a member that attended the ministry meeting
    '''
    ministry_meeting = models.ForeignKey(MinistryMeeting, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Member,blank = True,on_delete=models.CASCADE)



class ministryPhoto(models.Model):
    '''
        the photos of grouped under a group,
        can be tagged as belonging to a certain fellowship meeting that the attended
        can also be tagged as belonging or containing a certain member or members
    '''
    group = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    group_meeting = models.ForeignKey(MinistryMeeting,on_delete=models.CASCADE,null=True,blank=True)
    group_meeting_attendees = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True)
    photo = models.ImageField(upload_to='fellowships/', null=True)
