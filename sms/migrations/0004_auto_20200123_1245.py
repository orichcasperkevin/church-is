# Generated by Django 2.2 on 2020-01-23 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20200123_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsreceipients',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 23, 12, 45, 17, 919285)),
        ),
    ]