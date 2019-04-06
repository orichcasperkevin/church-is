# Generated by Django 2.2 on 2019-04-06 10:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('sermon', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('W', 'Written'), ('V', 'Video from Youtube')], max_length=1)),
                ('youtube_video_id', models.URLField(blank=True, verbose_name='Youtube Video Url')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('preached_by', models.CharField(blank=True, max_length=50)),
                ('featured_image', models.ImageField(upload_to='sermons/')),
                ('website', models.BooleanField(default=True, help_text='Publish on the website')),
                ('preached_by_member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
