# Generated by Django 2.2 on 2020-01-23 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0011_auto_20200123_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='last_credited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 23, 12, 47, 3, 855829)),
        ),
    ]