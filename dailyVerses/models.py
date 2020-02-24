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
