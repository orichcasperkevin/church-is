# Generated by Django 2.2 on 2020-02-07 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_churchgroup_anvil_space_only'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmeetingroster',
            name='attendee',
        ),
        migrations.RemoveField(
            model_name='groupmeetingroster',
            name='group_meeting',
        ),
        migrations.DeleteModel(
            name='GroupMeeting',
        ),
        migrations.DeleteModel(
            name='GroupMeetingRoster',
        ),
    ]
