# Generated by Django 2.2 on 2019-05-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190521_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='past',
            field=models.BooleanField(default=False),
        ),
    ]
