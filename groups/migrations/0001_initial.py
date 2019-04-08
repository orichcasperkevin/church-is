# Generated by Django 2.2 on 2019-04-08 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CellGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CellGroupMeeting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(help_text='The location of the host', max_length=200)),
                ('date', models.DateField(help_text='The visit date')),
            ],
        ),
        migrations.CreateModel(
            name='ChurchGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fellowship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FellowshipMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='The location of the host', max_length=200)),
                ('date', models.DateField(help_text='The visit date')),
                ('fellowship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Fellowship')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='The location of the meeting', max_length=200)),
                ('date', models.DateField(help_text='The visit date')),
            ],
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MinistryMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='The location of the meeting', max_length=200)),
                ('date', models.DateField(help_text='The visit date')),
            ],
        ),
        migrations.CreateModel(
            name='ministryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='fellowships/')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Ministry')),
                ('group_meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.MinistryMeeting')),
                ('group_meeting_attendees', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='MinistryMembership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Ministry')),
                ('ministry_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Role')),
            ],
        ),
        migrations.CreateModel(
            name='MinistryMeetingRoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('ministry_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.MinistryMeeting')),
            ],
        ),
        migrations.AddField(
            model_name='ministrymeeting',
            name='attendees',
            field=models.ManyToManyField(through='groups.MinistryMeetingRoster', to='member.Member'),
        ),
        migrations.AddField(
            model_name='ministrymeeting',
            name='host',
            field=models.ForeignKey(blank=True, help_text='Names of the host being visited.', on_delete=django.db.models.deletion.CASCADE, related_name='ministry_meeting_host', to='member.Member'),
        ),
        migrations.AddField(
            model_name='ministrymeeting',
            name='ministry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Ministry'),
        ),
        migrations.AddField(
            model_name='ministry',
            name='ministry_members',
            field=models.ManyToManyField(blank=True, through='groups.MinistryMembership', to='member.Member'),
        ),
        migrations.CreateModel(
            name='GroupPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='fellowships/')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.ChurchGroup')),
                ('group_meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.GroupMeeting')),
                ('group_meeting_attendees', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMeetingRoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('group_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.GroupMeeting')),
            ],
        ),
        migrations.AddField(
            model_name='groupmeeting',
            name='attendees',
            field=models.ManyToManyField(through='groups.GroupMeetingRoster', to='member.Member'),
        ),
        migrations.AddField(
            model_name='groupmeeting',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.ChurchGroup'),
        ),
        migrations.AddField(
            model_name='groupmeeting',
            name='host',
            field=models.ForeignKey(blank=True, help_text='Names of the host being visited.', on_delete=django.db.models.deletion.CASCADE, related_name='group_meeting_host', to='member.Member'),
        ),
        migrations.CreateModel(
            name='FellowshipPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='fellowships/')),
                ('fellowship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Fellowship')),
                ('fellowship_meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.FellowshipMeeting')),
            ],
        ),
        migrations.CreateModel(
            name='FellowshipMembership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('fellowship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Fellowship')),
                ('fellowship_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Role')),
            ],
        ),
        migrations.CreateModel(
            name='FellowshipMeetingRoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('fellowship_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.FellowshipMeeting')),
            ],
        ),
        migrations.AddField(
            model_name='fellowshipmeeting',
            name='fellowship_meeting_attendees',
            field=models.ManyToManyField(through='groups.FellowshipMeetingRoster', to='member.Member'),
        ),
        migrations.AddField(
            model_name='fellowshipmeeting',
            name='host',
            field=models.ForeignKey(help_text='Names of the host being visited.', on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='member.Member'),
        ),
        migrations.AddField(
            model_name='fellowship',
            name='fellowship_members',
            field=models.ManyToManyField(blank=True, through='groups.FellowshipMembership', to='member.Member'),
        ),
        migrations.CreateModel(
            name='ChurchGroupMembership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('church_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.ChurchGroup')),
                ('church_group_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Role')),
            ],
        ),
        migrations.AddField(
            model_name='churchgroup',
            name='group_members',
            field=models.ManyToManyField(blank=True, through='groups.ChurchGroupMembership', to='member.Member'),
        ),
        migrations.CreateModel(
            name='CellGroupPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='cell_groups/')),
                ('cell_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroup')),
                ('cell_group_meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroupMeeting')),
            ],
        ),
        migrations.CreateModel(
            name='CellGroupMembership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('CellGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroup')),
                ('cell_group_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Role')),
            ],
        ),
        migrations.CreateModel(
            name='CellGroupMeetingRoster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attendee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('cell_group_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroupMeeting')),
            ],
        ),
        migrations.AddField(
            model_name='cellgroupmeeting',
            name='attendees',
            field=models.ManyToManyField(through='groups.CellGroupMeetingRoster', to='member.Member'),
        ),
        migrations.AddField(
            model_name='cellgroupmeeting',
            name='cell_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.CellGroup'),
        ),
        migrations.AddField(
            model_name='cellgroupmeeting',
            name='host',
            field=models.ForeignKey(help_text='Names of the host being visited.', on_delete=django.db.models.deletion.CASCADE, related_name='cell_group_host', to='member.Member'),
        ),
        migrations.AddField(
            model_name='cellgroup',
            name='cell_group_members',
            field=models.ManyToManyField(blank=True, related_name='cell_group_members', through='groups.CellGroupMembership', to='member.Member'),
        ),
        migrations.AddField(
            model_name='cellgroup',
            name='minister',
            field=models.ForeignKey(help_text='minister in charge', on_delete=django.db.models.deletion.CASCADE, related_name='cell_group_minister', to='member.Member'),
        ),
    ]
