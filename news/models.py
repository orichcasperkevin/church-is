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
    date = models.DateField(default=timezone.now, help_text='Date of publishing of the article')
    author = models.CharField(max_length=100, help_text='Author of the news article')
    website = models.BooleanField(default=True, help_text='Publish on the website')

    class Meta:
        ordering = ('-date',)
