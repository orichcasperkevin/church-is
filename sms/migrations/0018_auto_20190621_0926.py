# Generated by Django 2.2 on 2019-06-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0017_auto_20190619_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='receipients',
            field=models.ManyToManyField(through='sms.SmsReceipients', to='member.Member'),
        ),
    ]
