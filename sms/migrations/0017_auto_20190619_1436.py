# Generated by Django 2.2 on 2019-06-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0016_auto_20190619_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='receipients',
            field=models.ManyToManyField(through='sms.SmsReceipients', to='member.Member'),
        ),
    ]
