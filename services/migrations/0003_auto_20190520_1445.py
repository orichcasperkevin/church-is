# Generated by Django 2.2 on 2019-05-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190520_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={},
        ),
        migrations.AlterModelOptions(
            name='serviceitem',
            options={'ordering': ('-date',)},
        ),
        migrations.RemoveField(
            model_name='service',
            name='date',
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='date',
            field=models.DateField(default='2019-05-01', help_text='The day of the service'),
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='venue',
            field=models.CharField(default='none', help_text='The day of the service', max_length=100),
        ),
    ]