from django.db import models
from django.utils import timezone
from djrichtextfield.models import RichTextField

from groups.models import ChurchGroup


class News(models.Model):
    '''
        News published by the church
    '''
    heading = models.CharField(max_length=100)
    article = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="The church")

    class Meta:
        ordering = ('-date',)
