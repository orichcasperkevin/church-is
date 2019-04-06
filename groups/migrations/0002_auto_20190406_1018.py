# Generated by Django 2.2 on 2019-04-06 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministrymeetingroster',
            name='attendee',
            field=models.ManyToManyField(blank=True, to='member.Member'),
        ),
        migrations.AddField(
            model_name='ministrymeetingroster',
            name='ministry_meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.MinistryMeeting'),
        ),
        migrations.AddField(
            model_name='ministrymeeting',
            name='host',
            field=models.ForeignKey(blank=True, help_text='Names of the host being visited.', on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AddField(
            model_name='ministrymeeting',
            name='ministry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Ministry'),
        ),
        migrations.AddField(
            model_name='ministry',
            name='ministry_members',
            field=models.ManyToManyField(blank=True, to='member.Member'),
        ),
        migrations.AddField(
            model_name='groupphoto',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.ChurchGroup'),
        ),
        migrations.AddField(
            model_name='groupphoto',
            name='group_meeting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.GroupMeeting'),
        ),
        migrations.AddField(
            model_name='groupphoto',
            name='group_meeting_attendees',
            field=models.ManyToManyField(blank=True, to='groups.GroupMeetingRoster'),
        ),
        migrations.AddField(
            model_name='groupmeetingroster',
            name='attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AddField(
            model_name='groupmeetingroster',
            name='group_meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.GroupMeeting'),
        ),
        migrations.AddField(
            model_name='groupmeeting',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.ChurchGroup'),
        ),
        migrations.AddField(
            model_name='groupmeeting',
            name='host',
            field=models.ForeignKey(blank=True, help_text='Names of the host being visited.', on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AddField(
            model_name='fellowshipphoto',
            name='fellowship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Fellowship'),
        ),
        migrations.AddField(
            model_name='fellowshipphoto',
            name='fellowship_meeting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.FellowshipMeeting'),
        ),
        migrations.AddField(
            model_name='fellowshipphoto',
            name='fellowship_meeting_attendees',
            field=models.ManyToManyField(blank=True, to='groups.FellowshipMeetingRoster'),
        ),
        migrations.AddField(
            model_name='fellowshipmeetingroster',
            name='attendee',
            field=models.ManyToManyField(blank=True, to='member.Member'),
        ),
        migrations.AddField(
            model_name='fellowshipmeetingroster',
            name='fellowship_meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.FellowshipMeeting'),
        ),
        migrations.AddField(
            model_name='fellowshipmeeting',
            name='fellowship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Fellowship'),
        ),
        migrations.AddField(
            model_name='fellowshipmeeting',
            name='host',
            field=models.ForeignKey(help_text='Names of the host being visited.', on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AddField(
            model_name='fellowship',
            name='fellowship_members',
            field=models.ManyToManyField(blank=True, to='member.Member'),
        ),
        migrations.AddField(
            model_name='churchgroup',
            name='group_members',
            field=models.ManyToManyField(blank=True, to='member.Member'),
        ),
        migrations.AddField(
            model_name='cellgroupphoto',
            name='cell_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroup'),
        ),
        migrations.AddField(
            model_name='cellgroupphoto',
            name='cell_group_meeting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroupMeeting'),
        ),
        migrations.AddField(
            model_name='cellgroupphoto',
            name='cell_group_meeting_attendee',
            field=models.ManyToManyField(blank=True, to='groups.CellGroupMeetingRoster'),
        ),
        migrations.AddField(
            model_name='cellgroupmeetingroster',
            name='attendee',
            field=models.ManyToManyField(blank=True, to='member.Member'),
        ),
        migrations.AddField(
            model_name='cellgroupmeetingroster',
            name='cell_group_meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroupMeeting'),
        ),
        migrations.AddField(
            model_name='cellgroupmeeting',
            name='cell_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroup'),
        ),
        migrations.AddField(
            model_name='cellgroupmeeting',
            name='host',
            field=models.ForeignKey(help_text='Names of the host being visited.', on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AddField(
            model_name='cellgroup',
            name='cell_group_members',
            field=models.ManyToManyField(blank=True, related_name='cell_group_members', to='member.Member'),
        ),
        migrations.AddField(
            model_name='cellgroup',
            name='minister',
            field=models.ForeignKey(help_text='minister in charge', on_delete=django.db.models.deletion.CASCADE, related_name='cell_group_minister', to='member.Member'),
        ),
    ]
