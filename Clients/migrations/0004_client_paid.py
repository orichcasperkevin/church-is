# Generated by Django 2.2 on 2019-12-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0003_auto_20191217_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]