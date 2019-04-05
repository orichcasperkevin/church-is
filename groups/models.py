from django.db import models
from member.models import Member


# Create your models here.
class Fellowship(models.Model):
    '''
        the name and description of the fellowship
    '''
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    fellowship_members = models.ManyToManyField(Member,blank = True)

    def __str__(self):
        return self.name


class FellowshipMeeting(models.Model):
    '''
        a fellowship as hosted by a member, at a location on a certain date
    '''
    fellowship = models.ForeignKey(Fellowship, on_delete=models.CASCADE)
    host = models.ForeignKey(Member,on_delete=models.CASCADE, help_text='Names of the host being visited.')
    location = models.CharField(max_length=200, help_text='The location of the host')
    date = models.DateField(help_text='The visit date')
    


class FellowshipMeetingRoster(models.Model):
    '''
        a member that attended the fellowship in the fellowshipRoster
    '''
    fellowship_meeting = models.ForeignKey(FellowshipMeeting, on_delete=models.CASCADE)
    attendee = models.ManyToManyField(Member,blank = True)
    


class FellowshipPhoto(models.Model):
    '''
        the photos of grouped under a fellowship,
        can be tagged as belonging to a certain fellowship meeting that the attended  
        can also be tagged as belonging or containing a certain member or members
    '''
    fellowship = models.ForeignKey(Fellowship, on_delete=models.CASCADE)
    fellowship_meeting = models.ForeignKey(FellowshipMeeting,on_delete=models.CASCADE,null=True,blank=True)
    fellowship_meeting_attendees = models.ManyToManyField(FellowshipMeetingRoster,blank=True)
    photo = models.ImageField(upload_to='fellowships/', null=True)



class CellGroup(models.Model):
    '''
        cell group
    '''
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    minister = models.ForeignKey(Member, on_delete = models.CASCADE,help_text='minister in charge',related_name="cell_group_minister")
    cell_group_members = models.ManyToManyField(Member,related_name='cell_group_members',blank = True)



class CellGroupMeeting(models.Model):
    '''
        a cell group as hosted by a member on a date 
    '''
    cell_group = models.ForeignKey(CellGroup, on_delete=models.CASCADE)
    host = models.ForeignKey(Member, on_delete = models.CASCADE, help_text='Names of the host being visited.')
    location = models.CharField(max_length=200, help_text='The location of the host')
    date = models.DateField(help_text='The visit date')
    


class CellGroupMeetingRoster(models.Model):
    '''
        a member that attended the cellGroup in the cellGroupRoster
    '''
    cell_group_meeting = models.ForeignKey(CellGroupMeeting, on_delete=models.CASCADE)
    attendee = models.ManyToManyField(Member,blank = True)



class CellGroupPhoto(models.Model):
    '''
        the photos grouped under a cell group,
        can be tagged as belonging to a certain cellGroup meeting that was attended 
        can also be tagged as belonging or containing a certain member or members
    '''
    cell_group = models.ForeignKey(CellGroup, on_delete=models.CASCADE)
    cell_group_meeting = models.ForeignKey(CellGroupMeeting,on_delete=models.CASCADE,null=True,blank=True)
    cell_group_meeting_attendee = models.ManyToManyField(CellGroupMeetingRoster,blank=True)
    photo = models.ImageField(upload_to='cell_groups/',)


class ChurchGroup(models.Model):
    '''
        the name and description of the group
    '''
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    group_members = models.ManyToManyField(Member,blank = True)

    def __str__(self):
        return self.name


class GroupMeeting(models.Model):
    '''
        a group meeting as hosted by a member, at a location on a certain date
    '''
    group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)
    host = models.ForeignKey(Member,on_delete=models.CASCADE, help_text='Names of the host being visited.',blank =True)
    location = models.CharField(max_length=200, help_text='The location of the meeting')
    date = models.DateField(help_text='The visit date')
    


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
    group_meeting_attendees = models.ManyToManyField(GroupMeetingRoster,blank=True)
    photo = models.ImageField(upload_to='fellowships/', null=True)


class Ministry(models.Model):
    '''
        the name and description of the group
    '''
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ministry_members = models.ManyToManyField(Member,blank = True)

    def __str__(self):
        return self.name


class MinistryMeeting(models.Model):
    '''
        a ministry meeting as hosted by a member, at a location on a certain date
    '''
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    host = models.ForeignKey(Member,on_delete=models.CASCADE, help_text='Names of the host being visited.',blank =True)
    location = models.CharField(max_length=200, help_text='The location of the meeting')
    date = models.DateField(help_text='The visit date')
    


class MinistryMeetingRoster(models.Model):
    '''
        a member that attended the ministry meeting
    '''
    ministry_meeting = models.ForeignKey(MinistryMeeting, on_delete=models.CASCADE)
    attendee = models.ManyToManyField(Member,blank = True)
    


class ministryPhoto(models.Model):
    '''
        the photos of grouped under a group,
        can be tagged as belonging to a certain fellowship meeting that the attended  
        can also be tagged as belonging or containing a certain member or members
    '''
    group = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    group_meeting = models.ForeignKey(MinistryMeeting,on_delete=models.CASCADE,null=True,blank=True)
    group_meeting_attendees = models.ManyToManyField(MinistryMeetingRoster,blank=True)
    photo = models.ImageField(upload_to='fellowships/', null=True)
