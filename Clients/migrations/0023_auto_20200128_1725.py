# Generated by Django 2.2 on 2020-01-28 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0022_auto_20200128_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='last_credited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 28, 17, 25, 11, 852817)),
        ),
    ]