# Generated by Django 2.2 on 2020-05-16 13:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('venue', models.CharField(default='none', help_text='The day of the service', max_length=100, null=True)),
                ('date', models.DateField(default='2019-05-01', help_text='The day of the service', null=True)),
                ('start', models.TimeField(help_text='write time e.g 00:22:19', null=True)),
                ('end', models.TimeField(help_text='write time e.g 00:22:19', null=True)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('start', models.TimeField(default=django.utils.timezone.now)),
                ('end', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(help_text='Title of the action to be performed', max_length=100)),
                ('value', models.CharField(help_text='The value to the title', max_length=200)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceType'),
        ),
    ]
