# Generated by Django 2.2 on 2019-06-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0012_auto_20190605_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='receipients',
            field=models.ManyToManyField(through='sms.SmsReceipients', to='member.Member'),
        ),
    ]