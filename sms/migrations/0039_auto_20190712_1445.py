# Generated by Django 2.2 on 2019-07-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0038_auto_20190703_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='receipients',
            field=models.ManyToManyField(through='sms.SmsReceipients', to='member.Member'),
        ),
    ]
