# Generated by Django 2.2 on 2019-05-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_past'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='past',
        ),
    ]