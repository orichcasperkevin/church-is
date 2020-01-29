# Generated by Django 2.2 on 2020-01-28 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('events', '0001_initial'),
        ('member', '0006_auto_20200109_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventattendinggroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.ChurchGroup'),
        ),
        migrations.AddField(
            model_name='eventattendedmember',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='eventattendedmember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
    ]
