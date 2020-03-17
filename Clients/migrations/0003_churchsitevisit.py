# Generated by Django 2.2 on 2020-03-17 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0002_clientdetail_last_credited'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchSiteVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('visitorID', models.CharField(blank=True, max_length=50, null=True)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Client')),
            ],
        ),
    ]
