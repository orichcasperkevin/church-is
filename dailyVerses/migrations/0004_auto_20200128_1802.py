# Generated by Django 2.2 on 2020-01-28 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyVerses', '0003_merge_20200128_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipientgroup',
            name='receipient_group',
        ),
        migrations.RemoveField(
            model_name='receipientgroup',
            name='verse',
        ),
        migrations.RemoveField(
            model_name='receipientmember',
            name='receipient_member',
        ),
        migrations.RemoveField(
            model_name='receipientmember',
            name='verse',
        ),
        migrations.DeleteModel(
            name='ExpectedToReceiveVerse',
        ),
        migrations.DeleteModel(
            name='ReceipientGroup',
        ),
        migrations.DeleteModel(
            name='ReceipientMember',
        ),
    ]