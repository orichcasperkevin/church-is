# Generated by Django 2.2 on 2019-05-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
