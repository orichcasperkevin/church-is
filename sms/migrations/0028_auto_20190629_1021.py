# Generated by Django 2.2 on 2019-06-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0027_auto_20190629_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='receipients',
            field=models.ManyToManyField(through='sms.SmsReceipients', to='member.Member'),
        ),
    ]
