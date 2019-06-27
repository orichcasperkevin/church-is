from django.db import models

from member.models import Member


# Create your models here.


class Sermon(models.Model):
    TYPE = (
        ('W', 'Written'),
        ('V', 'Video from Youtube')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    sermon = models.TextField(blank=True)
    type = models.CharField(max_length=1, choices=TYPE)
    youtube_video_id = models.URLField(blank=True, verbose_name='Youtube Video Url')
    date = models.DateField(auto_now_add=True)
    preached_by_member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    preached_by = models.CharField(max_length=50, blank=True, null=True)
    featured_image = models.ImageField(upload_to='sermons/', blank=True, null=True)
    website = models.BooleanField(default=True, help_text='Publish on the website')

    class Meta:
        ordering = ('-date',)
