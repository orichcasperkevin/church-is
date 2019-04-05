from django.db import models

from django.utils import timezone

from django.db import models
from member.models import Member
from groups.models import CellGroup,ChurchGroup,Ministry,Fellowship


class Verse(models.Model):
    text = models.TextField(help_text='The actual reading')
    verse = models.CharField(max_length=200, help_text='The verse in the Bible')
    day = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.verse) + ' on ' + str(self.day)



class ExpectedToReceiveVerse(models.Model):
    '''
        who is expected to receive the verse
    '''
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)
    who_will_receive = models.ManyToManyField(Member,blank = True)
    church_groups_receiving = models.ManyToManyField(ChurchGroup,blank = True)
    fellowships_receiving = models.ManyToManyField(Fellowship,blank = True)
    cell_groups_receiving = models.ManyToManyField(CellGroup,blank = True)
    ministries_receiving = models.ManyToManyField(Ministry,blank = True)


    