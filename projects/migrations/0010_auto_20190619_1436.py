# Generated by Django 2.2 on 2019-06-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20190523_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='recorded_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]