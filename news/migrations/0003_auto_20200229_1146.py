# Generated by Django 2.2 on 2020-02-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200229_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='website',
            field=models.BooleanField(default=True),
        ),
    ]
