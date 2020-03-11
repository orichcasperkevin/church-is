
from django.db import models

from groups.models import ChurchGroup
from member.models import Member

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    location = models.CharField(max_length=20, blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    @property
    def start(self):
        return self.start_datetime.strftime("%Y-%m-%d %H:%M")

    @property
    def end(self):
        return self.end_datetime.strftime("%Y-%m-%d %H:%M")

    @property
    def attendees(self):
        return MemberThatAttendedEvent.objects.filter(event_id=self.id).count() or 0


class GroupAttendingEvent(models.Model):
    '''
        what group is expected to attend the event
    '''
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)

class MemberThatAttendedEvent(models.Model):
    '''
        the members who attended the event
    '''
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
