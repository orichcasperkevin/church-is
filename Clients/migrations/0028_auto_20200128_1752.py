# Generated by Django 2.2 on 2020-01-28 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0027_auto_20200128_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='last_credited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 28, 17, 52, 47, 196212)),
        ),
    ]
