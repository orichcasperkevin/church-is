# Generated by Django 2.2 on 2020-02-24 08:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0051_auto_20200217_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='last_credited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 24, 11, 49, 12, 344515)),
        ),
        migrations.CreateModel(
            name='ChurchStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.TextField(max_length=150)),
                ('vission', models.TextField(max_length=150)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ChurchPeriodicTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.TextField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Client')),
            ],
            options={
                'ordering': ('-start',),
            },
        ),
        migrations.CreateModel(
            name='ChurchLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images/')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ChurchCoreValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Client')),
            ],
        ),
    ]
