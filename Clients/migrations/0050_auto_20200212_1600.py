# Generated by Django 2.2 on 2020-02-12 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0049_auto_20200212_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='last_credited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 12, 16, 0, 5, 726098)),
        ),
    ]
