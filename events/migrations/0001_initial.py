# Generated by Django 2.2 on 2019-04-10 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(help_text='SEO friendly slug', unique=True)),
                ('description', models.TextField(help_text='Description of the event')),
                ('date', models.DateTimeField(help_text='Date and Time of the event')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('website', models.BooleanField(default=True, help_text='Display on the website')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='events')),
                ('location', models.CharField(help_text='The location of the event ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ExpectedToAttendEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell_groups_coming', models.ManyToManyField(blank=True, to='groups.CellGroup')),
                ('church_groups_coming', models.ManyToManyField(blank=True, to='groups.ChurchGroup')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('fellowships_coming', models.ManyToManyField(blank=True, to='groups.Fellowship')),
                ('ministries_coming', models.ManyToManyField(blank=True, to='groups.Ministry')),
                ('who_is_coming', models.ManyToManyField(blank=True, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='EventRoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventAttendance')),
            ],
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='fellowships/')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('event_attendees', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.AddField(
            model_name='eventattendance',
            name='attendees',
            field=models.ManyToManyField(through='events.EventRoster', to='member.Member'),
        ),
        migrations.AddField(
            model_name='eventattendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]
