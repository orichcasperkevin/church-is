# Generated by Django 2.2 on 2020-02-10 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0040_auto_20200210_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='last_credited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 10, 13, 38, 27, 368566)),
        ),
    ]
