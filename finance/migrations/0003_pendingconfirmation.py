# Generated by Django 2.2 on 2019-11-26 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_delete_client'),
        ('finance', '0002_auto_20190822_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_message', models.TextField(max_length=500)),
                ('type', models.CharField(blank=True, choices=[('O', 'Offering'), ('T', 'Tithe')], max_length=2, null=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('confirming_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
    ]
