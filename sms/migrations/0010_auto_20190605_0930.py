# Generated by Django 2.2 on 2019-06-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0009_auto_20190605_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='receipients',
            field=models.ManyToManyField(through='sms.SmsReceipients', to='member.Member'),
        ),
    ]