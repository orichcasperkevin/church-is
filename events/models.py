from django.db import models
from member.models import Member
from groups.models import CellGroup,ChurchGroup,Ministry,Fellowship

# Create your models here.
class Event(models.Model):
    '''
        the name and description of the event
    '''
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text='SEO friendly slug')
    description = models.TextField(help_text='Description of the event')
    date = models.DateTimeField(help_text='Date and Time of the event')
    added_on = models.DateTimeField(auto_now_add=True)
    website = models.BooleanField(default=True, help_text='Display on the website')
    poster = models.ImageField(upload_to='events', null=True, blank=True)
    location = models.CharField(max_length=200, help_text='The location of the event ')


    def __str__(self):
        return self.name

class ExpectedToAttendEvent(models.Model):
    '''
        who is expected to attend the event
    '''
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    who_is_coming = models.ManyToManyField(Member,blank = True)
    church_groups_coming = models.ManyToManyField(ChurchGroup,blank = True)
    fellowships_coming = models.ManyToManyField(Fellowship,blank = True)
    cell_groups_coming = models.ManyToManyField(CellGroup,blank = True)
    ministries_coming = models.ManyToManyField(Ministry,blank = True)

class EventAttendance(models.Model):
    '''
        members that attended an event
    '''
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    attendees = models.ManyToManyField(Member,through='EventRoster')


class EventRoster(models.Model):
    '''
        members that attended the event 
    '''
    event = models.ForeignKey(EventAttendance, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Member,on_delete = models.CASCADE,blank = True)
    


class EventPhoto(models.Model):
    '''
        the photos of grouped under an event,
        can be tagged as belonging to a certain event meeting   
        can also be tagged as belonging or containing a certain member or members
    '''
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True,blank=True)
    event_attendees = models.ForeignKey(Member,on_delete= models.CASCADE,blank=True)
    photo = models.ImageField(upload_to='fellowships/', null=True)