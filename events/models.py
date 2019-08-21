
from django.db import models

from groups.models import ChurchGroup
from member.models import Member

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    location = models.CharField(max_length=20, blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    website = models.BooleanField(default=True)

    @property
    def start(self):
        start = self.start_datetime.strftime("%Y-%m-%d %H:%M")
        return start

    @property
    def end(self):
        end = self.end_datetime.strftime("%Y-%m-%d %H:%M")
        return end


class EventAttendingGroup(models.Model):
    '''
        what group is expected to attend the event
    '''
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)

class EventAttendedMember(models.Model):
    '''
        the members who attended the event
    '''
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
