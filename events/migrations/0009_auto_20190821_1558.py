# Generated by Django 2.2 on 2019-08-21 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20190821_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end',
            new_name='end_datetime',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start',
            new_name='start_datetime',
        ),
    ]
