# Generated by Django 2.2 on 2020-02-28 19:48

from django.db import migrations, models
import django.utils.timezone
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('article', djrichtextfield.models.RichTextField()),
                ('date', models.DateField(default=django.utils.timezone.now, help_text='Date of publishing of the article')),
                ('author', models.CharField(help_text='Author of the news article', max_length=100)),
                ('website', models.BooleanField(default=True, help_text='Publish on the website')),
                ('church_group', models.ManyToManyField(blank=True, to='groups.ChurchGroup')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
