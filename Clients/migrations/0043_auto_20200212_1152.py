# Generated by Django 2.2 on 2020-02-12 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0042_auto_20200210_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='last_credited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 12, 11, 52, 13, 777279)),
        ),
    ]
