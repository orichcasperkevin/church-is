# Generated by Django 2.2 on 2020-03-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchgroup',
            name='description',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='groupofchurchgroups',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
