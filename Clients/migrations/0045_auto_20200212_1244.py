# Generated by Django 2.2 on 2020-02-12 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0044_auto_20200212_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='last_credited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 12, 12, 44, 33, 634404)),
        ),
    ]
