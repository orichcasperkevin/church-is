# Generated by Django 2.2 on 2019-06-21 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20190619_0232'),
        ('finance', '0012_auto_20190619_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='tithe',
            name='recorded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tithe_recorded_by', to='member.Member'),
        ),
    ]