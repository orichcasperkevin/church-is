# Generated by Django 2.2 on 2020-05-16 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(default='admin', help_text='the app this message was sent from', max_length=160)),
                ('message', models.CharField(max_length=160)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('website', models.BooleanField(default=True, help_text='Publish on the website')),
                ('church_groups', models.ManyToManyField(blank=True, to='groups.ChurchGroup')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='SmsReceipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(default='0', max_length=20)),
                ('status', models.CharField(default='0', max_length=100)),
                ('receipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipient', to='member.Member')),
                ('sms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Sms')),
            ],
        ),
        migrations.CreateModel(
            name='SmsReceipientGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipient_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipient_group', to='sms.Sms')),
                ('sms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Sms')),
            ],
        ),
        migrations.AddField(
            model_name='sms',
            name='receipients',
            field=models.ManyToManyField(through='sms.SmsReceipients', to='member.Member'),
        ),
        migrations.AddField(
            model_name='sms',
            name='sending_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sending_member', to='member.Member'),
        ),
    ]
