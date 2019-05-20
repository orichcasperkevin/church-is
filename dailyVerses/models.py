from django.db import models

from django.utils import timezone

from django.db import models
from member.models import Member
from groups.models import CellGroup,ChurchGroup,Ministry,Fellowship


class Verse(models.Model):
    verse = models.CharField(max_length=200, help_text='The verse in the Bible')
    text = models.TextField(help_text='The actual reading')
    lesson = models.TextField(help_text='a lesson or moral from the verse')
    day = models.DateField(default=timezone.now)
    by = models.ForeignKey(Member,on_delete = models.CASCADE,blank = True,null = True)

class ExpectedToReceiveVerse(models.Model):
    '''
        who is expected to receive the verse
    '''
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)
    who_will_receive = models.ManyToManyField(Member, through = 'ReceipientMember',blank = True)
    church_groups_receiving = models.ManyToManyField(ChurchGroup,through='ReceipientGroup',blank = True)
    fellowships_receiving = models.ManyToManyField(Fellowship,through='ReceipientFellowship',blank = True)
    cell_groups_receiving = models.ManyToManyField(CellGroup,through='ReceipientCellGroup',blank = True)
    ministries_receiving = models.ManyToManyField(Ministry,through='ReceipientMinistry',blank = True)

class ReceipientMember(models.Model):
    verse = models.ForeignKey(ExpectedToReceiveVerse, on_delete=models.CASCADE)
    receipient_member = models.ForeignKey(Member, on_delete = models.CASCADE)

class ReceipientGroup(models.Model):
    verse = models.ForeignKey(ExpectedToReceiveVerse, on_delete=models.CASCADE)
    receipient_group = models.ForeignKey(ChurchGroup, on_delete = models.CASCADE)

class ReceipientFellowship(models.Model):
    verse = models.ForeignKey(ExpectedToReceiveVerse, on_delete=models.CASCADE)
    receipient_fellowship = models.ForeignKey(Fellowship, on_delete = models.CASCADE)

class ReceipientCellGroup(models.Model):
    verse = models.ForeignKey(ExpectedToReceiveVerse, on_delete=models.CASCADE)
    receipient_ceel_group = models.ForeignKey(CellGroup, on_delete = models.CASCADE)

class ReceipientMinistry(models.Model):
    verse = models.ForeignKey(ExpectedToReceiveVerse, on_delete=models.CASCADE)
    receipient_ministry = models.ForeignKey(Ministry, on_delete = models.CASCADE)
