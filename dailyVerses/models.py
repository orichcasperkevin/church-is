from django.db import models
from django.utils import timezone

from groups.models import ChurchGroup
from member.models import Member


class Verse(models.Model):
    verse = models.CharField(max_length=200, help_text='The verse in the Bible')
    text = models.TextField(help_text='The actual reading')
    lesson = models.TextField(help_text='a lesson or moral from the verse')
    day = models.DateField(default=timezone.now)
    by = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)


class ExpectedToReceiveVerse(models.Model):
    '''
        who is expected to receive the verse
    '''
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)
    church_groups_receiving = models.ManyToManyField(ChurchGroup, through='ReceipientGroup', blank=True)


class ReceipientMember(models.Model):
    verse = models.ForeignKey(ExpectedToReceiveVerse, on_delete=models.CASCADE)
    receipient_member = models.ForeignKey(Member, on_delete=models.CASCADE)


class ReceipientGroup(models.Model):
    verse = models.ForeignKey(ExpectedToReceiveVerse, on_delete=models.CASCADE)
    receipient_group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)
