# Generated by Django 2.2 on 2020-02-29 08:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(default='The church', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 29, 8, 44, 31, 326571, tzinfo=utc), help_text='Date of publishing of the article'),
        ),
    ]