from django.db import models
from django.utils import timezone
from djrichtextfield.models import RichTextField

from groups.models import ChurchGroup


class News(models.Model):
    '''
        News published by the church
    '''
    heading = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='news/', null=True, blank=True)
    church_group = models.ManyToManyField(ChurchGroup, blank=True)
    article = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="The church")
    website = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date',)
