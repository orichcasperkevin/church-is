# Generated by Django 2.2 on 2019-04-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duties', '0002_auto_20190405_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dutyroster',
            name='members',
            field=models.ManyToManyField(blank=True, to='member.Member'),
        ),
    ]
